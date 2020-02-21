from countpool import app, db
from flask import render_template, url_for, redirect, request, jsonify
from countpool.forms import NewTimer
from countpool.models import Timer



@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])

def home():

    # converting database query to dictionary
    timers = [row.__dict__ for row in Timer.query.all()]
    for item in timers:
        item.pop('_sa_instance_state')

    form = NewTimer()
    if form.validate_on_submit():

        goal = form.date.data

        # adding the form fields to the database
        new_timer = Timer(title=form.title.data, goal=goal)
        db.session.add(new_timer)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("home.html", form=form, timers=timers)

@app.route('/<id>/delete')
def delete_timer(id):

    timer = Timer.query.get(int(id))

    if timer is None:
        return redirect(url_for('home'))

    db.session.delete(timer)
    db.session.commit()

    return redirect(url_for('home'))
