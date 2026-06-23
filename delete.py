
def delete_latest_admission(conn, ama):
    try:
        cursor = conn.cursor(dictionary = True) 
        
        delete_query_patient = """
        DELETE FROM admission WHERE ama = %s AND date_time = (SELECT MAX(date_time) FROM admission WHERE ama = %s);
        """
        
        cursor.execute(delete_query_patient, (ama, ama))
        data = cursor.rowcount
        conn.commit()        
        cursor.close()
        
    except Exception as e:
        print(e)
        return 'error'

    return 'success'






