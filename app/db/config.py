#============================================================================
# Database schema and seed data configuration
#============================================================================

#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

#YOU NEED TO FIX AALL OF THE FOREIGN KEYS SO THEN THEY ARE FOREIGN KEYS AND LINKED< FIND INGUIDES UNDER DATA SHCEMA CONFIG


#-----------------------------------------------------
class PeopleTable:

    NAME = "people"

    SCHEMA = """
        CREATE TABLE people (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            project/s    TEXT NOT NULL,
            task/s  TEXT?,
            contact/s TEXT?
        )
    """
#-----------------------------------------------------    
#people
    SEED_DATA = """
        INSERT INTO people (name, contact/s)
        VALUES
            ("alex", "614859068\n64735287"),
            ("steve", "61888888\nsteveblockman@netmail.com.com"),
            """
#-----------------------------------------------------
class InvolvedTable:

    NAME = "involved"

    SCHEMA = """
        CREATE TABLE involved (        
            FOREIGN KEY(person_id) REFERENCES People(id)
            FOREIGN KEY(project_id) REFERENCES Projects(id)
        )
    """
#-----------------------------------------------------
class NotesTable:

    NAME = "notes"

    SCHEMA = """
        CREATE TABLE notes (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id   INTEGER,
            time_stamp    TEXT NOT NULL,
            content    TEXT NOT NULL

            FOREIGN KEY(person_id) REFERENCES People(id)
            FOREIGN KEY(project_id) REFERENCES Projects(id)
        )
    """
#-----------------------------------------------------
#notes
    SEED_DATA = """
        INSERT INTO notes (content)
        VALUES
            ("Alex your in charge of the word doc.")
            ("Steve can you add the powerpoint you made?")
    """
#-----------------------------------------------------
class FilesTable:

    NAME = "files"

    SCHEMA = """
        CREATE TABLE files (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            link   TEXT?,
            use   TEXT?,
            person_id   INTEGER,
            project_id   INTEGER
        )
    """    
#-----------------------------------------------------
#files
    SEED_DATA = """
        INSERT INTO files (name, link, use)
        VALUES
            ("document1", "https://docsz", "Reference sheet from our teacher")
            ("Template1.5", "https://realtemplatewebsite, "Template for writing notes on studied text")
    """
#-----------------------------------------------------
class ProjectsTable:
    
    NAME = "projects"

    SCHEMA = """
        CREATE TABLE projects (
            id      INTEGER,
            name   TEXT NOT NULL,
            deadline   TEXT?,
            status   TEXT NOT NULL
        )
    """    
#-----------------------------------------------------
#projects
    SEED_DATA = """
        INSERT INTO projects (name, deadline, status)
        VALUES
            ("English", "17/08/2079", "Unfinished")
            ("Group speech", "10/12/2027", "Finished")
            ("Enviro presentation", "none", "Unfinished")
    """
#-----------------------------------------------------

#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    PeopleTable,
    ProjectsTable,


]

