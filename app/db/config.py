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
class ProjectsTable:
    
    NAME = "projects"

    SCHEMA = """
        CREATE TABLE projects (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            deadline   TEXT,
            status   TEXT NOT NULL DEFAULT "Unfinished"
        )
    """    

    SEED_DATA = """
        INSERT INTO projects (name, deadline, status)
        VALUES
            ("English", "2079-08-17", "Unfinished"),
            ("Group speech", "2027-12-20", "Finished"),
            ("Enviro presentation", "none", "Unfinished")
    """
#-----------------------------------------------------
class PeopleTable:

    NAME = "people"

    SCHEMA = """
        CREATE TABLE people (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            contacts TEXT
        )
    """
    SEED_DATA = """
        INSERT INTO people (name, contacts)
        VALUES
            ("alex", "614859068\n64735287"),
            ("steve", "61888888\nsteveblockman@netmail.com")
    """

#-----------------------------------------------------
class InvolvedTable:

    NAME = "involved"

    SCHEMA = """
        CREATE TABLE involved (    
            person_id INTEGER NOT NULL,
            project_id INTEGER NOT NULL,  

            FOREIGN KEY(person_id) REFERENCES people(id),
            FOREIGN KEY(project_id) REFERENCES projects(id),
        
            PRIMARY KEY(person_id, project_id)
        )
    """

    SEED_DATA = """
        INSERT INTO involved (person_id, project_id)
        VALUES
            (1, 1),
            (1, 2),
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
            person_id INTEGER NOT NULL,
            project_id INTEGER NOT NULL,    

            FOREIGN KEY(person_id) REFERENCES People(id),
            FOREIGN KEY(project_id) REFERENCES Projects(id)
        )
    """

    SEED_DATA = """
        INSERT INTO notes (time_stamp, content, person_id, project_id)
        VALUES
            ("12:00", "Alex your in charge of the word doc.", 1, 2),
            ("01:00", "Steve can you add the powerpoint you made?", 1, 1)
    """
#-----------------------------------------------------
class FilesTable:

    NAME = "files"

    SCHEMA = """
        CREATE TABLE files (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT NOT NULL,
            link   TEXT,
            use   TEXT,
            person_id INTEGER NOT NULL,
            project_id INTEGER NOT NULL,    

            FOREIGN KEY(person_id) REFERENCES People(id),
            FOREIGN KEY(project_id) REFERENCES Projects(id)
        )
    """    
#-----------------------------------------------------
#files
    SEED_DATA = """
        INSERT INTO files (name, link, use, person_id, project_id)
        VALUES
            ("document1", "https://docsz", "Reference sheet from our teacher", "2", "3"),
            ("NoteTemplate", "https://realtemplatewebsite", "Template for writing notes on studied text", "1", "2")
    """
#-----------------------------------------------------

TABLES = [
    ProjectsTable,
    PeopleTable,
    InvolvedTable,
    NotesTable,
    FilesTable
]

