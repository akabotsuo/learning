from db.SQL import run_query


def followers_table_init():
    query = """ CREATE TABLE IF NOT EXISTS Followers (
                                     user varchar(255) PRIMARY KEY,
                                     points int NOT NULL,
                                     team varchar(255) NOT NULL
                                 ); """
    run_query(query)


def champions_table_init():
    query = """CREATE TABLE IF NOT EXISTS Champions (
                                 name varchar(255) PRIMARY KEY,
                                 nick varchar(255),
                                 cost integer,
                                 status_id integer NOT NULL,
                                 project_id integer NOT NULL,
                                 FOREIGN KEY (project_id) REFERENCES projects (id)
                             );"""
    run_query(query)


def database_table():
    query = """CREATE TABLE IF NOT EXISTS Database (
                                     name varchar(255) PRIMARY KEY,
                                     theme varchar(255),
                                     HOST varchar(255),
                                     PORT varchar(255),
                                     PASS varchar(255),
                                     identity varchar(255),
                                     channel varchar(255),
                                     related_table varchar(255)
                                 );"""
    run_query(query)
