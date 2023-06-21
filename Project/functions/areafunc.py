import psycopg2




def pullarea(process_area_name):
    connection = psycopg2.connect(
                    user="postgres",
                    password="postgrespostgres",
                    host="localhost",
                    port="5432",
                    database="workproject"
             )
    cursor = connection.cursor()
    query = "SELECT process_area_name FROM process_area WHERE process_area_name = %s"
    cursor.execute(query, (process_area_name,))
    process_area_name = cursor.fetchone()[0]
    return process_area_name 

