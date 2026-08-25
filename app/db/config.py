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

#-----------------------------------------------------
class PeopleTable:

    NAME = "people"

    SCHEMA = """
        CREATE TABLE people (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            project/s    TEXT NOT NULL,
            contact/s TEXT?
        )
    """
    SEED_DATA = """
        INSERT INTO people (id, name, project/s, contact/s)
        VALUES
            ("1", "alex", "1\n2\n4", "614859068\n64735287"),
            ("3", "steve", "1\n2\n6","61888888\nsteveblockman@netmail.com"),
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

    SEED_DATA = """
        INSERT INTO projects (id, name, deadline, status)
        VALUES
            ("1", "English", "17/08/2079", "Unfinished")
            ("2", "Group speech", "10/12/2027", "Finished")
            ("3", "Enviro presentation", "none", "Unfinished")
    """
#-----------------------------------------------------
class InvolvedTable:

    NAME = "involved"

    SCHEMA = """
        CREATE TABLE involved (        
            FOREIGN KEY(person_id) REFERENCES people(id),
            FOREIGN KEY(project_id) REFERENCES projects(id)
        )
    """

    SEED_DATA = """
        INSERT INTO involved (person_id, project_id)
        VALUES
            (1, 1)
            (1, 2)
            (2, 1)
    """
#-----------------------------------------------------
class NotesTable:

    NAME = "notes"

    SCHEMA = """
        CREATE TABLE notes (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            time_stamp    TEXT DEFAULT CURRENT_TIMESTAMP,
            content    TEXT NOT NULL,
            FOREIGN KEY(person_id) REFERENCES People(id),
            FOREIGN KEY(project_id) REFERENCES Projects(id)
        )
    """

    SEED_DATA = """
        INSERT INTO notes (id, time_stamp, content, person_id, project_id)
        VALUES
            ("1", "12:00", "Alex your in charge of the word doc.", 1, 2)
            ("2", "01:00", "Steve can you add the powerpoint you made?", 1, 1)
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
            FOREIGN KEY(person_id) REFERENCES People(id),
            FOREIGN KEY(project_id) REFERENCES Projects(id)
        )
    """    
#-----------------------------------------------------
#files
    SEED_DATA = """
        INSERT INTO files (id, name, link, use, person_id, project_id)
        VALUES
            ("1", "document1", "https://docsz", "Reference sheet from our teacher", "2", "3"),
            ("2", "Template1.5", "https://realtemplatewebsite, "Template for writing notes on studied text", "1", "2")
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

