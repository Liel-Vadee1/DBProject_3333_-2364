CREATE OR REPLACE FUNCTION assign_doctor_to_birth()
RETURNS TRIGGER AS $$
DECLARE
  matched_doctor_id INT;
BEGIN
  -- חפש רופא עם התמחות תואמת לסוג הלידה
  SELECT id_d INTO matched_doctor_id
  FROM doctor
  WHERE (birth_specialty = 'caesarean section'
  AND NEW.delivery_type = 'C-Section')
  OR (birth_specialty = 'normal birth'
  AND NEW.delivery_type = 'Natural')
  ORDER BY RANDOM()
  LIMIT 1;

  -- אם נמצא רופא תואם, הוסף אותו לטבלת midwife
  IF matched_doctor_id IS NOT NULL THEN
    INSERT INTO midwife (id_br, id_d)
    VALUES (NEW.id_br, matched_doctor_id);
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER auto_assign_doc
AFTER INSERT ON birth_record
FOR EACH ROW
EXECUTE FUNCTION assign_doctor_to_birth();

INSERT INTO baby (id_b, weigt, gender)
VALUES (510, 3.0, 'male');
INSERT INTO room (id_r, floor, availability) 
VALUES (450, 2, 'vacancy');
INSERT INTO maternity (id_m, name, age, phone, id_r)
VALUES (791, 'Sara Lev', 30, 523456789, 450);
INSERT INTO birth_record (id_br, delivery_type, birth_date, discharge_date, id_m, id_b)
VALUES (1002, 'C-Section', '2025-05-20', '2025-05-23', 791, 510);
SELECT * FROM midwife WHERE id_br = 1002;