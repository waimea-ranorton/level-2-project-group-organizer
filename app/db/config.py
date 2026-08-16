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

# class NoteTable:

#     NAME = "note"

#     SCHEMA = """
#         CREATE TABLE note (
#             id      INTEGER PRIMARY KEY AUTOINCREMENT,
#             title   TEXT NOT NULL,
#             body    TEXT,
#             pinned  INTEGER DEFAULT 0,
#             created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     """

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
class InvolvedTable:

    NAME = "involved"

    SCHEMA = """
        CREATE TABLE involved (
            project_id      INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id      INTEGER PRIMARY KEY AUTOINCREMENT
        )
    """
#-----------------------------------------------------
class NotesTable:

    NAME = "notes"

    SCHEMA = """
        CREATE TABLE notes (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id   INTEGER,
            project_id    INTEGER,
            time_stamp    TEXT NOT NULL
        )
    """
#-----------------------------------------------------
class FilesTable:

    NAME = "files"

    SCHEMA = """
        CREATE TABLE files (
            id      INTEGER,
            name   TEXT NOT NULL,
            type   TEXT NOT NULL,
            link   TEXT?,
            use   TEXT?,
            person_id   INTEGER,
            project_id   INTEGER
        )
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
#people
    SEED_DATA = """
        INSERT INTO people (title, pinned, body)
        VALUES
            ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
            ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
            ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
            ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
            ("Important!",    1, "Remember to backup your database regularly.")
    """
#-----------------------------------------------------
#involved
    SEED_DATA = """
        INSERT INTO involved (title, pinned, body)
        VALUES
            ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
            ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
            ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
            ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
            ("Important!",    1, "Remember to backup your database regularly.")
    """
#-----------------------------------------------------
#notes
    SEED_DATA = """
        INSERT INTO notes (title, pinned, body)
        VALUES
            ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
            ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
            ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
            ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
            ("Important!",    1, "Remember to backup your database regularly.")
    """
#-----------------------------------------------------
#files
    SEED_DATA = """
        INSERT INTO files (title, pinned, body)
        VALUES
            ("Welcome!",      1, "This is a demo application using Flask, Jinja and SQLite."),
            ("Shopping List", 0, "Milk\nBread\nEggs\nCheese"),
            ("Meeting Notes", 0, "Discussed project timeline.\n\nAction items:\n- Review design\n- Update docs"),
            ("Recipe: Pasta", 0, "Ingredients:\n- 500g pasta\n- Tomato sauce\n- Garlic\n\nCook pasta, add sauce, enjoy!"),
            ("Important!",    1, "Remember to backup your database regularly.")
    """
#-----------------------------------------------------
#projects
    SEED_DATA = """
        INSERT INTO projects (title, pinned, body)
        VALUES
            ("English", 0, "id\nname\ndeadline\nstatus\n)
    """
#-----------------------------------------------------

# Add more table classes here...



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
    NoteTable,
    # Add more tables here...
]

