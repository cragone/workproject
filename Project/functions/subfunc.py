import psycopg2


#query function for room info submission
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
    


#query function for equipment infor submission
def equip_note(room_name, ecn, status, expiry):
    connection = psycopg2.connect(
                    user="postgres",
                    password="postgrespostgres",
                    host="localhost",
                    port="5432",
                    database="workproject"
             )
    cursor = connection.cursor()
    query = "INSERT INTO equipmentstatus (room_name, ecn, status, expiry) values (%s, %s, %s, %s); COMMIT;"
    cursor.execute(query, (room_name, ecn, status, expiry))
    try:
        
        cursor.close()
        connection.close()
        return 'good'
    except:
        
        return None
    
