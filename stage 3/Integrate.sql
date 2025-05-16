CREATE EXTENSION IF NOT EXISTS postgres_fdw;

CREATE SERVER matan_noam_server
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'localhost', dbname 'Matan&Noam', port '5432');

CREATE USER MAPPING FOR current_user
SERVER matan_noam_server
OPTIONS (user 'Lielv', password 'lielvadee3055');

CREATE FOREIGN TABLE Department(
    department_id INT,
    department_name Varchar(100)
) SERVER matan_noam_server
OPTIONS (schema_name 'public', table_name 'Department');

CREATE FOREIGN TABLE CancerPatient (
    patient_id INT,
    full_name VARCHAR(100),
    birth_date DATE,
    gender VARCHAR(10),
    phone VARCHAR(20),
    email VARCHAR(200),
	registration_date DATE
) SERVER matan_noam_server
OPTIONS (schema_name 'public', table_name 'CancerPatient');

CREATE FOREIGN TABLE Diagnosis (
    diagnosis_id INT,
    patient_id INT,
    cancer_type VARCHAR(100),
    diagnosis_date DATE,
    stage VARCHAR(50),
	staff_id INT
) SERVER matan_noam_server
OPTIONS (schema_name 'public', table_name 'Diagnosis');

CREATE FOREIGN TABLE TreatmentPlan(
    plan_id INT,
    diagnosis_id INT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(50),
    goal VARCHAR(500),
	protocol VARCHAR(100)
) SERVER matan_noam_server
OPTIONS (schema_name 'public', table_name 'TreatmentPlan');

CREATE FOREIGN TABLE TreatmentSession(
    session_id INT,
    plan_id INT,
    room VARCHAR(50),
    treatment_type VARCHAR(100),
    administered_by INT
) SERVER matan_noam_server
OPTIONS (schema_name 'public', table_name 'TreatmentSession');

CREATE FOREIGN TABLE OncologyStaff(
    staff_id INT,
    specialization VARCHAR(100),
    full_name VARCHAR(50),
    role VARCHAR(100),
    department_id INT
) SERVER matan_noam_server
OPTIONS (schema_name 'public', table_name 'OncologyStaff');

CREATE FOREIGN TABLE SideEffectReport(
    report_id INT,
    session_id INT,
    symptom VARCHAR(50),
    severity INT,
    report_date DATE,
	staff_id INT
) SERVER matan_noam_server
OPTIONS (schema_name 'public', table_name 'SideEffectReport');


