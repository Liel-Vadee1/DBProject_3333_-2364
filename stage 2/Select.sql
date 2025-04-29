
-- This SQL query retrieves the year and month of birth from the birth_record table,
-- counts the total number of births for each month, and orders the results by year and month.
SELECT 
  EXTRACT(YEAR FROM birth_date) AS birth_year,
  EXTRACT(MONTH FROM birth_date) AS birth_month,
  COUNT(*) AS total_births
FROM birth_record
GROUP BY EXTRACT(YEAR FROM birth_date), EXTRACT(MONTH FROM birth_date)
ORDER BY birth_year, birth_month;

-- This SQL query retrieves the average weight of babies for each delivery type from the birth_record and baby tables.
-- It groups the results by delivery type and calculates the average weight for each group.
SELECT 
  delivery_type,
  AVG(b.weigt) AS avg_weight
FROM birth_record br
JOIN baby b ON br.id_b = b.id_b
GROUP BY delivery_type;

-- This SQL query retrieves the names of doctors who have more than 10 years of seniority,
-- the birth record ID, the birth date, and the name of the mother.
SELECT 
  d.name AS doctor_name,
  br.id_br,
  br.birth_date,
  m.name AS mother_name
FROM doctor d
JOIN midwife mw ON d.id_d = mw.id_d
JOIN birth_record br ON mw.id_br = br.id_br
JOIN maternity m ON br.id_m = m.id_m
WHERE d.seniority > 10;

-- This SQL query retrieves the names of mothers who have given birth in rooms with more than one mother.
-- It counts the number of mothers in each room and lists their names.
SELECT 
  r.id_r,
  COUNT(m.id_m) AS mothers_in_room,
  LISTAGG(m.name, ', ') WITHIN GROUP (ORDER BY m.name) AS mother_names
FROM room r
JOIN maternity m ON r.id_r = m.id_r
GROUP BY r.id_r
HAVING COUNT(m.id_m) > 1;

-- This SQL query retrieves the names of bybes who were discharged within 3 days of birth,
-- along with their birth date, discharge date, weight, and the name of the mother.
SELECT 
  b.id_b,
  br.birth_date,
  br.discharge_date,
  b.weigt,
  m.name AS mother_name
FROM birth_record br
JOIN baby b ON br.id_b = b.id_b
JOIN maternity m ON br.id_m = m.id_m
WHERE br.discharge_date - br.birth_date < 3;

-- This SQL query retrieves the names of nurses who have been assigned to more than 2 rooms,
-- along with the count of rooms assigned to each nurse.
SELECT 
  n.id_n,
  n.name,
  COUNT(at.id_r) AS rooms_assigned
FROM nurse n
JOIN attending_to at ON n.id_n = at.id_n
GROUP BY n.id_n, n.name
HAVING COUNT(at.id_r) > 2;

-- This SQL query retrieves the names of mothers who have given birth to more than one baby,
-- along with the count of babies for each mother.
SELECT 
  m.name,
  COUNT(br.id_br) AS birth_count
FROM maternity m
JOIN birth_record br ON m.id_m = br.id_m
GROUP BY m.name
HAVING COUNT(br.id_br) > 1;

-- This SQL query retrieves the names of doctors who have assisted in more than 5 births,
-- along with the count of births for each doctor.
SELECT 
  TO_CHAR(birth_date, 'Day') AS weekday,
  COUNT(*) AS births_per_day
FROM birth_record
GROUP BY TO_CHAR(birth_date, 'Day')
ORDER BY births_per_day DESC;