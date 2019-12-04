import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'MS3_project'
app.config["MONGO_URI"] = 'mongodb+srv://rOOtUser:betteroption@myfirstcluster-97xkz.mongodb.net/MS3_project?retryWrites=true&w=majority'
# os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/firstSteps')
def firstSteps():
    return render_template('firstSteps.html', firstSteps=mongo.db.firstSteps.find())


@app.route('/myProblem', methods=['GET', 'POST'])
def myProblem():
    if request.method == 'GET':
        return render_template('myProblem.html', myProblem=mongo.db.myProblem.find())
    else:
        insert_myProblem = mongo.db.myProblem
        insert_myProblem.insert_one(request.form.to_dict())
        return redirect(url_for('index'))


@app.route('/alias')
def alias():
    return render_template("alias.html")


@app.route('/aliasConfirmed')
def aliasConfirmed():
    return render_template("aliasConfirmed.html")


@app.route('/tasks')
def tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/habits')
def habits():
    return render_template("habits.html", habit_manager=mongo.db.habit_manager.find())

@app.route('/addHabits')
def addHabits():
    return render_template('addHabits.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)