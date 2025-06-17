import psycopg2
from psycopg2 import sql
import tkinter.messagebox as messagebox
from config import DB_CONFIG

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(**DB_CONFIG)
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")
            return False
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query, params=None, fetch=True):
        try:
            self.cursor.execute(query, params)
            if fetch:
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return True
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Database Error", f"Query execution failed: {str(e)}")
            return None if fetch else False
    
    def execute_procedure(self, procedure_name, params=None):
        try:
            if params:
                self.cursor.callproc(procedure_name, params)
            else:
                self.cursor.execute(f"CALL {procedure_name}()")
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Database Error", f"Procedure execution failed: {str(e)}")
            return False
    
    def execute_function(self, function_call):
        try:
            self.cursor.execute(function_call)
            result = self.cursor.fetchall()
            self.connection.commit()
            return result
        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Database Error", f"Function execution failed: {str(e)}")
            return None

    # CRUD Operations for Maternity table
    def get_all_maternity(self):
        query = """
        SELECT m.id_m, m.name, m.age, m.phone, m.id_r, r.floor, r.availability 
        FROM maternity m 
        LEFT JOIN room r ON m.id_r = r.id_r 
        ORDER BY m.id_m
        """
        return self.execute_query(query)
    
    def insert_maternity(self, name, age, phone, room_id):
        query = "INSERT INTO maternity (id_m, name, age, phone, id_r) VALUES ((SELECT COALESCE(MAX(id_m), 0) + 1 FROM maternity), %s, %s, %s, %s)"
        return self.execute_query(query, (name, age, phone, room_id), fetch=False)
    
    def update_maternity(self, id_m, name, age, phone, room_id):
        query = "UPDATE maternity SET name = %s, age = %s, phone = %s, id_r = %s WHERE id_m = %s"
        return self.execute_query(query, (name, age, phone, room_id, id_m), fetch=False)
    
    def delete_maternity(self, id_m):
        # First delete related birth records and midwife records
        self.execute_query("DELETE FROM midwife WHERE id_br IN (SELECT id_br FROM birth_record WHERE id_m = %s)", (id_m,), fetch=False)
        self.execute_query("DELETE FROM birth_record WHERE id_m = %s", (id_m,), fetch=False)
        query = "DELETE FROM maternity WHERE id_m = %s"
        return self.execute_query(query, (id_m,), fetch=False)
    
    # CRUD Operations for Baby table
    def get_all_babies(self):
        query = "SELECT id_b, weigt, gender FROM baby ORDER BY id_b"
        return self.execute_query(query)
    
    def insert_baby(self, weight, gender):
        query = "INSERT INTO baby (id_b, weigt, gender) VALUES ((SELECT COALESCE(MAX(id_b), 0) + 1 FROM baby), %s, %s)"
        return self.execute_query(query, (weight, gender), fetch=False)
    
    def update_baby(self, id_b, weight, gender):
        query = "UPDATE baby SET weigt = %s, gender = %s WHERE id_b = %s"
        return self.execute_query(query, (weight, gender, id_b), fetch=False)
    
    def delete_baby(self, id_b):
        # First delete related birth records and midwife records
        self.execute_query("DELETE FROM midwife WHERE id_br IN (SELECT id_br FROM birth_record WHERE id_b = %s)", (id_b,), fetch=False)
        self.execute_query("DELETE FROM birth_record WHERE id_b = %s", (id_b,), fetch=False)
        query = "DELETE FROM baby WHERE id_b = %s"
        return self.execute_query(query, (id_b,), fetch=False)
    
    # CRUD Operations for Birth Record table (linking table)
    def get_all_birth_records(self):
        query = """
        SELECT br.id_br, br.delivery_type, br.birth_date, br.discharge_date, 
               m.name as mother_name, b.gender as baby_gender, b.weigt as baby_weight
        FROM birth_record br
        JOIN maternity m ON br.id_m = m.id_m
        JOIN baby b ON br.id_b = b.id_b
        ORDER BY br.id_br
        """
        return self.execute_query(query)
    
    def insert_birth_record(self, delivery_type, birth_date, discharge_date, mother_id, baby_id):
        query = """
        INSERT INTO birth_record (id_br, delivery_type, birth_date, discharge_date, id_m, id_b) 
        VALUES ((SELECT COALESCE(MAX(id_br), 0) + 1 FROM birth_record), %s, %s, %s, %s, %s)
        """
        return self.execute_query(query, (delivery_type, birth_date, discharge_date, mother_id, baby_id), fetch=False)
    
    def update_birth_record(self, id_br, delivery_type, birth_date, discharge_date, mother_id, baby_id):
        query = """
        UPDATE birth_record 
        SET delivery_type = %s, birth_date = %s, discharge_date = %s, id_m = %s, id_b = %s 
        WHERE id_br = %s
        """
        return self.execute_query(query, (delivery_type, birth_date, discharge_date, mother_id, baby_id, id_br), fetch=False)
    
    def delete_birth_record(self, id_br):
        # First delete related midwife records
        self.execute_query("DELETE FROM midwife WHERE id_br = %s", (id_br,), fetch=False)
        query = "DELETE FROM birth_record WHERE id_br = %s"
        return self.execute_query(query, (id_br,), fetch=False)
    
    # Get available rooms
    def get_available_rooms(self):
        query = "SELECT id_r, floor, availability FROM room WHERE availability = 'vacancy' ORDER BY id_r"
        return self.execute_query(query)
    
    # Get mothers and babies for dropdowns
    def get_mothers_list(self):
        query = "SELECT id_m, name FROM maternity ORDER BY name"
        return self.execute_query(query)
    
    def get_babies_list(self):
        query = "SELECT id_b, gender, weigt FROM baby ORDER BY id_b"
        return self.execute_query(query)
    
    # Query 1: Room and Night Shift Nurse Assignment
    def query_night_shift_nurses(self):
        query = """
        SELECT 
          r.id_r AS room_id,
          m.name AS mother_name,
          n.name AS nurse_name,
          n.shift_hours
        FROM room r
        JOIN maternity m ON r.id_r = m.id_r
        JOIN attending_to at ON r.id_r = at.id_r
        JOIN nurse n ON at.id_n = n.id_n
        WHERE n.shift_hours = 'night'
          AND r.id_r IN (
            SELECT id_r
            FROM maternity
            GROUP BY id_r
            HAVING COUNT(*) = 1
          )
        ORDER BY r.id_r
        """
        return self.execute_query(query)
    
    # Query 2: Birth Type and Baby Weight Correlation
    def query_birth_weight_analysis(self):
        query = """
        SELECT 
            br.delivery_type,
            COUNT(br.id_br) AS total_births,
            ROUND(AVG(b.weigt)::numeric, 2) AS avg_baby_weight
        FROM birth_record br
        JOIN baby b ON br.id_b = b.id_b
        WHERE br.birth_date >= CURRENT_DATE - INTERVAL '1 year'
        GROUP BY br.delivery_type
        """
        return self.execute_query(query)