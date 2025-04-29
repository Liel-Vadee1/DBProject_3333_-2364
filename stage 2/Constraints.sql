--1
ALTER TABLE maternity
MODIFY name VARCHAR(50) NOT NULL;

INSERT INTO maternity (id_m, name, age, phone, id_r) VALUES (999, NULL, 30, 123456789, 1);
-- cannot insert NULL


--2
ALTER TABLE maternity
ADD CONSTRAINT chk_mother_age CHECK (age BETWEEN 14 AND 55);

INSERT INTO maternity (id_m, name, age, phone, id_r) VALUES (888, 'שרה', 10, 123456789, 1);
-- CHECK constraint violated

--3
ALTER TABLE room
MODIFY availability DEFAULT 'available';

INSERT INTO room (id_r, floor) VALUES (777, 1);
-- availability is set to 'available' by default

