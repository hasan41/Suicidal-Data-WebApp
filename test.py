import psycopg2
import pandas as pd

db_conc = {
    "host"      : "suicide-db.cfnbykir9i4m.us-east-1.rds.amazonaws.com",
    "database"  : "suicide",
    "user"      : "postgres",
    "password"  : "Password"
}

def connect(db_conc):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**db_conc)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn


def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df





# ----------------------- DATA PROCESSMENT ----------

# Connect to the database
conn = connect(db_conc)
column_names = ["Id", "country", "year", "sex", "age", "suicides_no", "population", "suicides/100k_pop", "country_year", "HDI_for_year", "gdp_for_year", "gdp_per_capita", "generation"]
# Execute the "SELECT *" query
df = postgresql_to_dataframe(conn, "select * from public.suicide", column_names)
df.head()