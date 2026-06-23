
def patient_search_by_ama(conn, ama: str):
    try:
        cursor = conn.cursor(dictionary = True) #to get results as dictionaries
        insert_query_patient = """
        SELECT * FROM patient WHERE ama = %s;
        """
        cursor.execute(insert_query_patient, (ama, ))
        data = cursor.fetchone()
        # pprint.pprint(data)
        
        cursor.close()
        
    except Exception as e:
        print(e)
        return None

    if data:
        return data
    else:
        return None
    

def latest_admission_by_ama(conn, ama):
    try:
        cursor = conn.cursor(dictionary = True) #to get results as dictionaries
        

        insert_query_patient = """
        SELECT * FROM admission WHERE ama = %s AND date_time = (SELECT MAX(date_time) FROM admission WHERE ama = %s) LIMIT 1;
        """
        cursor.execute(insert_query_patient, (ama, ama))
        data = cursor.fetchone()
        
        cursor.close()
        
    except Exception as e:
        print(e)
        return None

    if data:
        return data
    else:
        return None



