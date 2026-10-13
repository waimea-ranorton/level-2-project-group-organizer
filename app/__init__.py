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
# Home page - Show recent things
#-----------------------------------------------------------
#===========================================================
@app.get("/")
def show_project():
    with connect_db() as db:
        sql = """
                SELECT id, name, deadline, status
                FROM projects
                ORDER BY name DESC
        """
        params = ()
        tasks = db.execute(sql, params).fetchall()

        return render_template("pages/home.jinja")
#===========================================================
@app.get("/projects")
def show_projects():
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

        return render_template("pages/project_list.jinja", project=projects)
#===========================================================
@app.get("/project_new")
def show_project_form():
    return render_template("pages/project_new.jinja")

#===========================================================
@app.post("/project_new")
def process_project_form():
    #get form data
        name = request.form.get("name", "unknown").strip() #default value if no species
        deadline = request.form.get("deadline", "unknown").strip()

        with connect_db() as db:
            sql = """
                INSERT INTO projects (name, deadline)
                VALUES (?, ?)
            """
            params = (name, deadline)

            #run query
            db.execute(sql, params)

            flash(f"Project {name} added successfully")

            #done, return to list
            return redirect("/project_new")

#===========================================================
@app.get("/calendar")
def show_calendar():
    with connect_db() as db:
        sql = """
            SELECT name, deadline
            FROM projects
            WHERE status = 'Unfinished'
        """
        params = ()
        projects = db.execute(sql, params).fetchall()

        return render_template("pages/calendar.jinja", projects=projects)
#===========================================================  
@app.get("/calendar/finished")
def show_calendar_finished():
    with connect_db() as db:
        sql = """
            SELECT name, deadline
            FROM projects
            WHERE status = 'Finished'
        """
        params = ()
        projects = db.execute(sql, params).fetchall()

        return render_template("pages/calendar_finished.jinja", projects=projects)
#===========================================================   
@app.get("/calendar/past_due")
def show_calendar_past_due():
    with connect_db() as db:
        sql = """
            SELECT name, deadline
            FROM projects
            WHERE status = 'Past_due'
        """
        params = ()
        projects = db.execute(sql, params).fetchall()

        return render_template("pages/calendar_past_due.jinja", projects=projects)
#===========================================================      
@app.get("/settings")
def show_settings():
    return render_template("pages/settings.jinja")
#===========================================================    

@app.get("/project/<int:id>/delete")
def delete_a_project(id):
    with connect_db() as db:
        ##delete project using its id
        sql = """
            DELETE FROM projects
            WHERE id = ?
        """
        params = (id,)
        db.execute(sql, params)  

        flash("Project deleted", "success")
##back to list
        return redirect("/calendar")        

#----------------------------------------------------------- 
#-Let user update a project to finsihed

#-----------------------------------------------------------        

# Configure the app
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

