import sqlite3

database = "C:\sqlite\sqlite-tools-win32-x86-3200100\Followers.db"


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return None


def exe_sql(conn, query, get=False):
    try:
        c = conn.cursor()
        c.execute(query)

        if get:
            data = c.fetchall()
            return data

        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)


def run_query(query, get=False):
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        if get:
            return exe_sql(conn, query, get)

        exe_sql(conn, query)
    else:
        print("Error! cannot create the database connection.")
    pass


def view_db():
    query = '''SELECT * FROM Followers;'''
    return run_query(query, True)


def view_table(table):
    query = "SELECT * FROM '%s';" % table
    return run_query(query, True)


def new_follower(table, user_name, team):
    query = "INSERT INTO " + table + " VALUES('%s', '%d', '%s');" % (user_name, 0, team)
    run_query(query)


def get_user(table, user):
    query = "SELECT * FROM " + table + " WHERE user='" + user + "';"
    try:
        return run_query(query, True)[0]
    except:
        return None


def drop_table(table):
    query = 'DROP TABLE ' + table + ";"
    run_query(query)


def new_host(table, name, theme, host, port, pass_key, identity, channel, table_name):
    query = 'INSERT INTO ' + table + " VALUES('%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s');" % (
        name, theme, host, port, pass_key, identity, channel, table_name)
    run_query(query)


def update_points(table, user, points):
    query = 'UPDATE ' + table + " SET points='%d' WHERE user='%s';" % (points, user)
    run_query(query)
