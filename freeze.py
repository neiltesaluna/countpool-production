from countpool import app
from flask_frozen import Freezer

static_app = Freezer(app)

if __name__ == "__main__":
    static_app.freeze()
