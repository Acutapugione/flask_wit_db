from .. import app
from flask import render_template
from database import Session
from database.models import Student
from sqlalchemy import select


@app.route("/student")
def student_list():
    with Session.begin() as session:
        context = {
            "items": session.scalars(select(Student)).all()
        }
        return render_template("list.html", **context)


