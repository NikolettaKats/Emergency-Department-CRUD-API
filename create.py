import datetime
import mysql.connector
from flask import jsonify
from http import HTTPStatus


#CREATE FUNCTION FOR PATIENT
def create_patient(conn, patient_data):
    try:
        cursor = conn.cursor()
        insert_query_patient = """
        INSERT INTO patient (ama, first_name, last_name, father_name, asf_foreas, city,
        address, tk, date_of_birth, phone_number, career, religion, citizenship, Rname, Rlastname, Raddress, Rphone, allergies,
        infectious_disaese, past_admission_reason, father_mother_history, brother_history, husband_kid_history)
        VALUES (%(ama)s, %(first_name)s, %(last_name)s, %(father_name)s, %(asf_foreas)s, %(city)s,
        %(address)s, %(tk)s, %(date_of_birth)s, %(phone_number)s, %(career)s, %(religion)s, %(citizenship)s, %(Rname)s,
        %(Rlastname)s, %(Raddress)s, %(Rphone)s, %(allergies)s, %(past_admission_reason)s, %(father_mother_history)s,
        %(brother_hitory)s, %(husband_kid_history)s ) ;
        """

        cursor.execute(insert_query_patient, patient_data)
        conn.commit()
        cursor.close()
    
    except mysql.connector.errors.Error as e:
        print(e)
        return 'error'
    return jsonify ({'message': 'Η εγγραφή ολοκληρώθηκε με επιτυχία'}), HTTPStatus.CREATED

  


#CREATE FUNCTION FOR ADMISSION
def create_admission(conn, admission_data):
    try:
        cursor = conn.cursor()
        insert_query_admission = """
        INSERT INTO admission (date_time, kind_of_admission, kind_of_transport, accompanied_by, information, possible_diagnosis, symptoms,
        BP, HR, temperature, vbreath, height, weight, ama)
        VALUES (%(date_time)s, %(kind_of_admission)s, %(kind_of_transport)s, %(accompanied_by)s, %(information)s,
        %(possible_diagnosis)s, %(symptoms)s, %(BP)s, %(HR)s, %(temperature)s, %(breath)s, %(height)s, %(weight)s, %(ama)s );
        """

        
        admission_data['date_time'] = datetime.datetime.now().isoformat()
        
        cursor.execute(insert_query_admission, admission_data)
        conn.commit()
        cursor.close()

    
    except mysql.connector.errors.Error as e:
        print(e)
        return 'error' 
    return jsonify ({'message': 'Η εγγραφή ολοκληρώθηκε με επιτυχία'}), HTTPStatus.CREATED