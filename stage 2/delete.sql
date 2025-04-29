-- this script deletes all records from the maternity table that do not have a corresponding record in the birth_record table.
-- It uses a subquery to find all id_m values in the birth_record table and deletes any records in the maternity table that do not match those id_m values.
DELETE FROM maternity
WHERE id_m NOT IN (
  SELECT id_m FROM birth_record
);

-- this script deletes all records from the baby table that have a weight less than 2.0 and do not have a corresponding record in the birth_record table.
-- It uses a subquery to find all id_b values in the birth_record table and deletes any records in the baby table that do not match those id_b values.
DELETE FROM baby
WHERE weigt < 2.0
AND id_b NOT IN (
  SELECT id_b FROM birth_record
);

-- this script deletes all records from the doctor table that do not have a corresponding record in the midwife table.
-- It uses a subquery to find all id_d values in the midwife table and deletes any records in the doctor table that do not match those id_d values.
DELETE FROM doctor
WHERE id_d NOT IN (
  SELECT DISTINCT id_d FROM midwife
);


