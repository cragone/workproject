import psycopg2


#function for room submission info
def room_note(room_name, room_notes, datetime):
    connection = psycopg2.connect(
                    user="postgres",
                    password="postgrespostgres",
                    host="localhost",
                    port="5432",
                    database="workproject"
             )
    cursor = connection.cursor()
    query = "INSERT INTO notes (room_name, room_notes, datetime) values (%s, %s, %s); COMMIT;"

    try:
        cursor.execute(query, (room_name, room_notes, datetime))
        cursor.close()
        connection.close()
        return 'good'
    except:
        
        return None
    
#Making function for equipment submission info