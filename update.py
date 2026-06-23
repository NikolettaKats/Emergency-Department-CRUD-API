
def update_patient(conn, patient_data):
    try:
        cursor = conn.cursor(dictionary = True) #to get results as dictionaries
        if 'ama' not in patient_data:
            return 'error'
        
        update_query_patient = """
        UPDATE patient SET first_name=%(first_name)s, last_name=%(last_name)s, father_name=%(father_name)s, asf_foreas=%(asf_foreas)s, city=%(city)s,
        address=%(address)s, tk=%(tk)s, date_of_birth=%(date_of_birth)s, phone_number=%(phone_number)s, career=%(career)s, religion=%(religion)s,
        citizenship=%(citizenship)s, Rname=%(Rname)s, Rlastname=%(Rlastname)s, Raddress=%(Raddress)s, Rphone=%(Rphone)s, allergies=%(allergies)s,
        infectious_disease=%(infectious_disease)s, past_admission_reason=%(past_admission_reason)s, father_mother_history=%(father_mother_history)s,
        brother_history=%(brother_history)s, husband_kid_history=%(husband_kid_history)s WHERE ama=%(ama)s;
        """

        cursor.execute(update_query_patient, patient_data)
        data = cursor.rowcount
        conn.commit()
        cursor.close()
        
    except Exception as e:
        print(e)
        return None

    return data



def update_admission(conn, admission_data):
    try:
        cursor = conn.cursor(dictionary = True) #to get results as dictionaries
        if 'ama' not in admission_data:
            return 'error'
        
        update_query_admission = """
        UPDATE admission SET kind_of_admission=%(kind_of_admission)s, kind_of_transport=%(kind_of_transport)s, accompanied_by=%(accompanied_by)s,
        information=%(information)s, possible_diagnosis=%(possible_diagnosis)s, symptoms=%(symptoms)s, BP=%(BP)s, HR=%(HR)s, temperature=%(temperature)s,
        breath=%(breath)s, height=%(height)s, weight=%(weight)s WHERE ama=%(ama)s AND date_time=(SELECT MAX(date_time) FROM admission WHERE ama=%(ama)s);
        """

        cursor.execute(update_query_admission, admission_data)
        data = cursor.rowcount
        conn.commit()
        cursor.close()
        
    except Exception as e:
        print(e)
        return None

    return data



if __name__ == "__main__":
    from db import create_connection
    conn = create_connection()
    patient_data = {
        'ama' : '12345',
        'first_name' : 'John',
        'last_name' : 'Doe',
        'father_name' : 'Mike',
        'asf_foreas' : 'test_insurance',
        'city' : 'test_city',
        'address' : 'test_address',
        'tk' : 12345,
        'date_of_birth': '1199/05/24',
        'phone_number' : '1234567890',
    }
 
    print(update_patient(conn, patient_data))
    conn.close()
    