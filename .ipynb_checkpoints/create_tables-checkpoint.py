import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    Description: Creates and connects to the sparkifydb.

    Arguments:
        None

    Returns:
        cur: the cursor to sparkifydb
        conn: the connection to sparkifydb
    """       
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Description: Drops each table using the queries in `drop_table_queries` list.

    Arguments:
        cur: the cursor to sparkifydb
        conn: the connection to sparkifydb

    Returns:
        None
    """  
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Description: Creates each table using the queries in `create_table_queries` list. 

    Arguments:
        cur: the cursor to sparkifydb
        conn: the connection to sparkifydb

    Returns:
        None
    """  
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Description: Establishes connection with the sparkify database and gets
    cursor to it. Drops (if exists) and Creates the sparkify database.
    Drops all the tables and creates all tables needed.
    Finally, closes the connection.

    Arguments:
        None

    Returns:
        None
    """ 
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()