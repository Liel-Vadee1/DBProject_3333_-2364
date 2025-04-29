-- this script updates the availability of rooms in the maternity department
-- to 'not available' if there are more than one maternity patients in the same room
UPDATE room
SET availability = 'not available'
WHERE id_r IN (
  SELECT id_r
  FROM maternity
  GROUP BY id_r
  HAVING COUNT(*) > 1
);

-- this script updates the shifts of nurses in the maternity department
-- to 'long shift' if they are attending to more than two patients
UPDATE nurse
SET shift_hours = 'long shift'
WHERE id_n IN (
  SELECT id_n
  FROM attending_to
  GROUP BY id_n
  HAVING COUNT(*) > 2
);

-- this script updates the phone number of maternity patients
-- to '999999999' if they have more than one birth record
UPDATE maternity
SET phone = 999999999
WHERE id_m IN (
  SELECT id_m
  FROM birth_record
  GROUP BY id_m
  HAVING COUNT(*) > 1
);


