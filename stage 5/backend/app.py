from flask import Flask, request, jsonify
from flask_cors import CORS
from database import DatabaseManager
from config import DB_CONFIG 
import psycopg2

#app = Flask(__name__)
app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

db = DatabaseManager()
if not db.connect():
    print("Failed to connect to the database.")
    exit(1)

@app.route('/')
def login_page():
    return app.send_static_file('login.html')


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': 'Missing username or password'}), 400

    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            database=DB_CONFIG['database'],
            user=username,
            password=password
        )
        conn.close()
        return jsonify({'success': True, 'message': 'Login successful'}), 200

    except Exception as e:
        print("Login error:", e)
        return jsonify({'success': False, 'message': 'Invalid credentials or DB connection failed'}), 401

# ----------- Maternity Routes -----------

@app.route('/api/maternity', methods=['GET'])
def get_maternity():
    results = db.get_all_maternity()
    
    return jsonify(results)

@app.route('/api/maternity/<int:id_m>', methods=['GET'])
def get_maternity_by_id(id_m):
    result = db.get_maternity_by_id(id_m)
    return jsonify(result)

@app.route('/api/maternity', methods=['POST'])
def add_maternity():
    data = request.json
    success = db.insert_maternity(data['name'], data['age'], data['phone'], data['id_r'])
    return jsonify({'success': success})


@app.route('/api/maternity/<int:id_m>', methods=['PUT'])
def update_maternity(id_m):
    data = request.json
    success = db.update_maternity(id_m, data['name'], data['age'], data['phone'], data['id_r'])
    return jsonify({'success': success})


@app.route('/api/maternity/<int:id_m>', methods=['DELETE'])
def delete_maternity(id_m):
    success = db.delete_maternity(id_m)
    return jsonify({'success': success})


# ----------- Baby Routes -----------

@app.route('/api/baby', methods=['GET'])
def get_babies():
    results = db.get_all_babies()
    return jsonify(results)


@app.route('/api/baby/<int:id_b>', methods=['GET'])
def get_baby_by_id(id_b):
    result = db.get_baby_by_id(id_b)
    return jsonify(result)


@app.route('/api/baby', methods=['POST'])
def add_baby():
    data = request.json
    success = db.insert_baby(data['weigt'], data['gender'])
    return jsonify({'success': success})


@app.route('/api/baby/<int:id_b>', methods=['PUT'])
def update_baby(id_b):
    data = request.json
    success = db.update_baby(id_b, data['weigt'], data['gender'])
    return jsonify({'success': success})


@app.route('/api/baby/<int:id_b>', methods=['DELETE'])
def delete_baby(id_b):
    success = db.delete_baby(id_b)
    return jsonify({'success': success})


# ----------- Birth Record Routes -----------

@app.route('/api/birth_records', methods=['GET'])
def get_birth_records():
    results = db.get_all_birth_records()
    return jsonify(results)

@app.route('/api/birth_records/<int:id_br>', methods=['GET'])
def get_birth_records_by_id(id_br):
    result = db.get_birth_records_by_id(id_br)
    return jsonify(result)

@app.route('/api/birth_records', methods=['POST'])
def add_birth_record():
    data = request.json
    success = db.insert_birth_record(
        data['delivery_type'],
        data['birth_date'],
        data['discharge_date'],
        data['id_m'],
        data['id_b']
    )
    return jsonify({'success': success})


@app.route('/api/birth_records/<int:id_br>', methods=['PUT'])
def update_birth_record(id_br):
    data = request.json
    success = db.update_birth_record(
        id_br,
        data['delivery_type'],
        data['birth_date'],
        data['discharge_date'],
        data['id_m'],
        data['id_b']
    )
    if success:
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False, 'message': 'Failed to update birth record'}), 400

    #return jsonify({'success': success})


@app.route('/api/birth_records/<int:id_br>', methods=['DELETE'])
def delete_birth_record(id_br):
    success = db.delete_birth_record(id_br)
    return jsonify({'success': success})


# ----------- Rooms and Dropdowns -----------

@app.route('/api/rooms/available', methods=['GET'])
def get_available_rooms():
    results = db.get_available_rooms()
    return jsonify(results)


@app.route('/api/mothers/list', methods=['GET'])
def get_mothers_list():
    results = db.get_mothers_list()
    return jsonify(results)


@app.route('/api/babies/list', methods=['GET'])
def get_babies_list():
    results = db.get_babies_list()
    return jsonify(results)

@app.route('/api/baby/unassigned', methods=['GET'])
def get_unassigned_babies():
    query = """
        SELECT id_b, weigt, gender FROM baby
        WHERE id_b NOT IN (
            SELECT id_b FROM birth_record
            WHERE id_b IS NOT NULL
        )
    """
    results = db.execute_query(query)

    # המרה לרשימת מילונים
    result_list = [
        {"id_b": row[0], "weigt": row[1], "gender": row[2]}
        for row in results
    ]

    return jsonify(result_list)


# ----------- Queries -----------

@app.route('/api/queries/night_shift_nurses', methods=['GET'])
def query_night_shift_nurses():
    results = db.query_night_shift_nurses()
    return jsonify(results)


@app.route('/api/queries/birth_weight_analysis', methods=['GET'])
def query_birth_weight_analysis():
    results = db.query_birth_weight_analysis()
    return jsonify(results)


@app.route('/api/queries/monthly_birth_statistics', methods=['GET'])
def query_birth_statistics():
    results = db.query_birth_statistics()
    return jsonify(results)


# ----------- procedure -----------
@app.route('/api/procedure/assign_rooms_and_return', methods=['POST'])
def run_assign_rooms():
    result = db.execute_procedure_with_refcursor('assign_rooms_and_return')
    if result is False:
        return jsonify({'success': False, 'message': 'Procedure assign_rooms_and_return execution failed.'}), 500
    else:
        return jsonify({'success': True, 'result': result})

@app.route('/api/procedure/get_department_summary', methods=['POST'])
def run_department_summary():
    result = db.execute_procedure_with_refcursor('get_department_summary')
    if result is False:
        return jsonify({'success': False, 'message': 'Procedure get_department_summary execution failed.'}), 500
    else:
        return jsonify({'success': True, 'result': result})
    
    
# ----------- function -----------
@app.route('/api/function', methods=['POST'])
def run_function():
    data = request.json
    function_call = data.get('function_call')
    if not function_call:
        return jsonify({'success': False, 'message': 'Missing function_call string.'}), 400

    result = db.execute_function(function_call)
    if result is not None:
        return jsonify({'success': True, 'result': result})
    else:
        return jsonify({'success': False, 'message': 'Function execution failed.'}), 500


# ----------- Main -----------

if __name__ == '__main__':
    app.run(debug=True, port=8080)
