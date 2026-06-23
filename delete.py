
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



# def delete_patient(conn, patient_data):
#     try:
#         cursor = conn.cursor(dictionary = True) #to get results as dictionaries
#         # insert_query_patient = """
#         # SELECT * FROM admission WHERE ama = %s ORDER BY date_time DESC LIMIT 1;
#         # """
#         if 'ama' not in patient_data:
#             return 'error'
        
#         delete_query_patient = """
#         DELETE * FROM patient WHERE ama = %s;
#         """
        
#         cursor.execute(delete_query_patient, patient_data)
#         data = cursor.rowcount
#         conn.commit()
#         #
#         # pprint.pprint(data)
        
#         cursor.close()
        
#     except Exception as e:
#         print(e)
#         return None

#     return data



# def delete_admission(conn, admission_data):
#     try:
#         cursor = conn.cursor(dictionary = True) #to get results as dictionaries
#         # insert_query_patient = """
#         # SELECT * FROM admission WHERE ama = %s ORDER BY date_time DESC LIMIT 1;
#         # """
#         if 'ama' not in admission_data:
#             return 'error'
        
#         delete_query_admission = """
#         DELETE * FROM admission WHERE ama = %s; 
#         """

#         cursor.execute(delete_query_admission, admission_data)
#         data = cursor.rowcount
#         conn.commit()
#         #
#         # pprint.pprint(data)
        
#         cursor.close()
        
#     except Exception as e:
#         print(e)
#         return None

#     return data


