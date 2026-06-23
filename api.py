from flask import Flask, request, jsonify, g
import mysql.connector
import pprint
import datetime

from create import create_patient, create_admission
from db import create_connection
from read import patient_search_by_ama, latest_admission_by_ama
from update import update_patient, update_admission
from delete import delete_latest_admission 


app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = create_connection()
    return g.db

def get_cursor():
    return get_db().cursor()

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/patient', methods=['POST'])
def add_patient():
    data = request.json
    pprint.pprint(data)

    result = create_patient(get_db(), data)
    

    return jsonify({"status": result}) 

@app.route('/admission', methods = ['POST'])
def add_admission():
    data=request.json
    pprint.pprint(data)

    result = create_admission(get_db(), data)

    return jsonify({"status" : result})



@app.route('/update', methods=['POST'])
def update_endpoint():
    data = request.json
    print(data)

    rows_affected = update_patient(get_db(), data)
    # print(rows_affected)
    if rows_affected > 1:
        return jsonify({'status': 'error'})
    
    rows_affected = update_admission(get_db(), data)
    # print(rows_affected)
    if rows_affected != 1:
        return jsonify({'status': 'error'})
    
    return jsonify({'status': 'success'})
        

@app.route('/fyllo-asthenous', methods=['POST'])
def fyllo_asthenous():
    data = request.json
    
    pprint.pprint(data)

    patient_data = data['patient_data']
    admission_data = data['admission_data']

    
    if patient_search_by_ama(get_db(), patient_data['ama']):
        print('PATIENT EXITS, APPENDIN NEW ADMISSION')
    else:
        result = create_patient(get_db(), patient_data)
        if result == 'error':
            return jsonify({'status': result, 'message': 'Patient creation failed'}) # somehting gone wrong
    
    # add AMA to admission data
    admission_data['ama'] = patient_data['ama']
    if admission_data['date_time'] == '':
        admission_data['date_time'] = datetime.datetime.now().isoformat()
    
    result = create_admission(get_db(), admission_data)

    return jsonify({"status" : result})

@app.route('/patient', methods=['GET'])
def get_patient():
    ama = request.args.get('ama')
    
    result = patient_search_by_ama(get_db(), ama)
    latest_admission = latest_admission_by_ama(get_db(), ama)

    if result is None:  
        result= {}         
    if latest_admission is None:
        latest_admission = {} 

    return jsonify(result | latest_admission)


@app.route('/latest-admission', methods=['GET'])
def get_latest_admission():
    ama = request.args.get(ama)


@app.route('/delete-latest-admission' , methods = ['GET'])
def delete_admission():
    #   data= request.json
    ama = request.args.get('ama')

    if ama is None:
        return jsonify ({'status': 'error', 'message': 'AMA not provided'})
        
    
    result = delete_latest_admission(get_db(), ama)
    if result == 'success':
        return jsonify ({'status': 'success', 'message': 'Patient deleted successfully'})
    else:
        return jsonify ({'status': 'success', 'message': 'Failed to delete patient'})


@app.route('/delete-patient', methods = ['GET'])
def delete_patient():
    data= request.json
    ama = data.get( 'ama')
    if ama is None:
        return jsonify ({'status': 'error', 'message': 'AMA not provided'})
        
    result = delete_patient (get_db(), ama)
    latest_admission = latest_admission_by_ama (get_db(), ama)

    if result is None:
        result = {}
    if latest_admission is None:
        latest_admission = {}

    if result == 'success':
        return jsonify ({'status': 'success', 'message': 'Patient deleted successfully'})
    else:
        return jsonify ({'status': 'success', 'message': 'Failed to delete patient'})
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)



