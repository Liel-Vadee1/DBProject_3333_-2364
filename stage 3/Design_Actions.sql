-- update table doctor
ALTER TABLE doctor
ADD COLUMN department_id INT;

--
ALTER TABLE doctor
ADD CONSTRAINT chk_doctor_only_maternity
CHECK (department_id = 7);

UPDATE doctor
SET department_id = 7;

Select *
from doctor;


-- update table nurse
ALTER TABLE nurse
ADD COLUMN department_id INT;

--
ALTER TABLE nurse
ADD CONSTRAINT chk_nurse_only_maternity
CHECK (department_id = 7);

UPDATE nurse
SET department_id = 7;

Select *
from nurse;


----------------------------------------------
SELECT 
    d.name AS doctor_name,
    dr.department_name
FROM 
    doctor d
JOIN 
    Department dr ON d.department_id = dr.department_id;

