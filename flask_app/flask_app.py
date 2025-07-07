from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('home_flask_app.html')


@app.route("/enumeration_task")
def enumeration_task():
    return render_template('include/main_enumeration_task.html')


@app.route("/gonogo_task")
def gonogo_task():
    return render_template('include/main_gonogo_task.html')


@app.route("/loadblindness_task")
def loadblindness_task():
    return render_template('include/main_loadblindness_task.html')


@app.route("/memorability_task1")
def memorability_task1():
    return render_template('include/main_memorability_task1.html')


@app.route("/memorability_task2")
def memorability_task2():
    return render_template('include/main_memorability_task2.html')


@app.route("/moteval_task")
def moteval_task():
    return render_template('include/main_moteval_task.html')


@app.route("/taskswitch_task")
def taskswitch_task():
    return render_template('include/main_taskswitch_task.html')


@app.route("/workingmemory_task")
def workingmemory_task():
    return render_template('include/main_workingmemory_task.html')
