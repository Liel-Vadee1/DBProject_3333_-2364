CREATE TABLE Maternity (
    id INT PRIMARY KEY,
    name VARCHAR2(100),
    age INT,
    phone VARCHAR2(20)
);

CREATE TABLE Baby (
    id INT PRIMARY KEY,
    gender VARCHAR2(10),
    weight NUMERIC(5,2)
);

CREATE TABLE Doctor (
    id INT PRIMARY KEY,
    name VARCHAR2(100),
    experience_years INT,
    birth_type VARCHAR2(50)
);

CREATE TABLE Nurse (
    id INT PRIMARY KEY,
    name VARCHAR2(100),
    shift VARCHAR2(20)
);

CREATE TABLE Room (
    id INT PRIMARY KEY,
    floor_number INT,
    availability VARCHAR2(10)
);

CREATE TABLE BirthRecord (
    id INT PRIMARY KEY,
    maternity_id INT REFERENCES Maternity(id),
    baby_id INT REFERENCES Baby(id),
    doctor_id INT REFERENCES Doctor(id),
    nurse_id INT REFERENCES Nurse(id),
    room_id INT REFERENCES Room(id),
    birth_date DATE,
    discharge_date DATE,
    birth_type VARCHAR2(50)
);