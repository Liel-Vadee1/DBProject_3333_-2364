ALTER TABLE room
ALTER COLUMN availability SET DEFAULT 'VACANT';

INSERT INTO Room (id_r, floor) VALUES(403, 2);

select *
from room
where id_r = 403;

----------------------------------------------------
ALTER TABLE maternity
ADD CONSTRAINT chk_age CHECK (age BETWEEN 14 AND 55);

INSERT INTO Maternity (id_m, name, age, phone,id_r) VALUES
(403, 'Ruth Cohen', 12, '050123457',3);

---------------------------------------------------
ALTER TABLE baby
ALTER COLUMN weigt SET NOT NULL;

INSERT INTO Baby (id_b, gender) VALUES
(403, 'Male');




