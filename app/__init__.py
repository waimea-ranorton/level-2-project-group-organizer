#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/")
def show_tasks():
    with connect_db() as db:
        sql = """
            SELECT id, name, deadline, status
            FROM projects
            ORDER BY name DESC
        """
        params = ()
        notes = db.execute(sql, params).fetchall()

        flash("Test message")
        flash("Test SUCCESS message", "success")
        flash("Test INFO message", "info")
        flash("Test WARNING message", "warning")
        flash("Test ERROR message", "error")

        return render_template("pages/note_list.jinja", notes=notes)


#===========================================================
@app.get("/project")
def show_project():
    return render_template("pages/project.jinja")

#===========================================================
@app.get("/project/new")
def show_project_form():
    return render_template("pages/project_new.jinja")

#===========================================================
@app.post("/project/new")
def process_project_form():
    with connect_db() as db:
        #get form data
        name = request.form.get("name", "unknown").strip() #default value if no species
        priority = request.form.get("priority", "unknown").strip()

        #connect to the DB
        with connect_db() as db:
            sql = """
                INSERT INTO projects (priority, name)
                VALUES (?, ?)
            """
            params = (name, priority)

            #run query
            db.execute(sql, params)

            flash(f"project {name} added successfully")

            #done, return to list
            return redirect("/")

#===========================================================
@app.get("/calendar")
def show_calendar():
    return render_template("pages/calendar.jinja")
#===========================================================    
@app.get("/settings")
def show_settings():
    return render_template("pages/settings.jinja")
#===========================================================    
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

