INSERT INTO Maternity (id, name, age, phone) VALUES
(1, 'Ruth Cohen', 32, '0501234567'),
(2, 'Noa Levi', 28, '0529876543'),
(3, 'Yael Israeli', 35, '0543216789');

INSERT INTO Baby (id, gender, weight) VALUES
(1, 'Male', 3.2),
(2, 'Female', 2.8),
(3, 'Male', 3.5);

INSERT INTO Doctor (id, name, experience_years, delivery_type) VALUES
(1, 'Dr. Michael Baruch', 10, 'C-section'),
(2, 'Dr. Sharon Levi', 15, 'Natural'),
(3, 'Dr. Ronit Cohen', 8, 'C-section');

INSERT INTO Nurse (id, name, shift) VALUES
(1, 'Esther Raviv', 'Morning'),
(2, 'Oren Cohen', 'Evening'),
(3, 'Dana Levi', 'Night');

INSERT INTO Room (id, floor, availability) VALUES
(1, 2, 'Available'),
(2, 3, 'Occupied'),
(3, 1, 'Available');

INSERT INTO BirthRecord (id, maternity_id, baby_id, doctor_id, nurse_id, room_id, birth_date, discharge_date, birth_type) VALUES
(1, 1, 1, 1, 1, 1, TO_DATE('2024-03-10', 'YYYY-MM-DD'), TO_DATE('2024-03-12', 'YYYY-MM-DD'), 'C-section'),
(2, 2, 2, 2, 2, 2, TO_DATE('2024-03-15', 'YYYY-MM-DD'), TO_DATE('2024-03-18', 'YYYY-MM-DD'), 'Natural'),
(3, 3, 3, 3, 3, 3, TO_DATE('2024-03-20', 'YYYY-MM-DD'), TO_DATE('2024-03-22', 'YYYY-MM-DD'), 'C-section');
