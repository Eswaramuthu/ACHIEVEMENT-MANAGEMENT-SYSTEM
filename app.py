from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/student")
def student():
    return render_template("student.html")


@app.route("/teacher")
def teacher():
    return render_template("teacher.html")


@app.route("/student-new")
def student_new():
    return render_template("student_new.html")


@app.route("/teacher-new")
def teacher_new():
    return render_template("teacher_new.html")


@app.route("/teacher-achievements")
def teacher_achievements():
    return render_template("teacher_achievement.html")

@app.route("/student-achievements")
def student_achievements():
    return render_template("student_achievements.html")


@app.route("/student-dashboard")
def student_dashboard():
    return render_template("student_dashboard.html")


@app.route("/teacher-dashboard")
def teacher_dashboard():
    return render_template("teacher_dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)