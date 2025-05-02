SELECT 
  r.id_r AS room_id,
  m.name AS mother_name,
  n.name AS nurse_name,
  n.shift_hours
FROM room r
JOIN maternity m ON r.id_r = m.id_r
JOIN attending_to at ON r.id_r = at.id_r
JOIN nurse n ON at.id_n = n.id_n
WHERE n.shift_hours = 'night'
  AND r.id_r IN (
    SELECT id_r
    FROM maternity
    GROUP BY id_r
    HAVING COUNT(*) = 1
  )
ORDER BY r.id_r;
---------------------------------------------
SELECT 
  m.id_m, 
  m.name, 
  br.birth_date, 
  br.delivery_type,
  COUNT(br.id_b) AS babies_born
FROM maternity m
JOIN birth_record br ON m.id_m = br.id_m
GROUP BY 
  m.id_m, 
  m.name, 
  br.birth_date, 
  br.delivery_type
HAVING COUNT(br.id_b) > 1
ORDER BY br.birth_date;

---------------------------------------------
SELECT 
    br.delivery_type,
    COUNT(br.id_br) AS total_births,
    ROUND(AVG(b.weigt)::numeric, 2) AS avg_baby_weight
FROM birth_record br
JOIN baby b ON br.id_b = b.id_b
WHERE br.birth_date >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY br.delivery_type;

----------------------------------------------
SELECT 
    n.id_n AS nurse_id,
    n.name AS nurse_name,
    COUNT(DISTINCT b.id_b) AS total_babies,
    COUNT(DISTINCT at.id_r) AS total_rooms,
    ROUND(AVG(b.weigt)::numeric, 2) AS avg_baby_weight
FROM nurse n
JOIN attending_to at ON n.id_n = at.id_n  
JOIN maternity m ON at.id_r = m.id_r 
JOIN birth_record br ON m.id_m = br.id_m 
JOIN baby b ON br.id_b = b.id_b 
GROUP BY n.id_n, n.name  
HAVING 
    COUNT(DISTINCT b.id_b) / NULLIF(COUNT(DISTINCT at.id_r), 0) = 2
ORDER BY 
    total_babies DESC;

-----------------------------------------------
SELECT 
  EXTRACT(YEAR FROM birth_date) AS birth_year,
  EXTRACT(MONTH FROM birth_date) AS birth_month,
  COUNT(*) AS total_births
FROM birth_record
GROUP BY EXTRACT(YEAR FROM birth_date), EXTRACT(MONTH FROM birth_date)
ORDER BY birth_year, birth_month;

------------------------------------------------
SELECT br.id_br, d.name, d.birth_specialty
FROM birth_record br
JOIN midwife mw ON br.id_br = mw.id_br
JOIN doctor d ON mw.id_d=d.id_d
WHERE  EXTRACT(YEAR FROM br.birth_date) = 2025
  AND br.delivery_type = 'Vaginal'
  AND d.birth_specialty = 'normal birth'
EXCEPT
SELECT br.id_br, d.name, d.birth_specialty
FROM birth_record br
JOIN midwife mw ON br.id_br = mw.id_br
JOIN doctor d ON mw.id_d=d.id_d
WHERE d.seniority <  2;

-----------------------------------------------
SELECT 
  b.id_b AS baby_id,
  b.gender AS baby_gender,
  m.name AS mother_name,
  m.age AS mother_age,
  br.delivery_type AS delivery_type,
  ( 
    SELECT COUNT(*) 
    FROM birth_record br_inner
    WHERE br_inner.id_m = m.id_m
  ) AS total_babies
FROM birth_record br
JOIN baby b ON br.id_b = b.id_b
JOIN maternity m ON br.id_m = m.id_m
WHERE 
  b.gender = 'M'  
  AND m.age > 30     
  AND br.delivery_type = 'C-Section'  
  AND (SELECT COUNT(*)
    FROM birth_record br_inner
    WHERE br_inner.id_m = m.id_m) < 2  
ORDER BY m.age DESC;  

----------------------------------------------------
SELECT 
    n.name AS nurse_name, 
    n.shift_hours AS nurse_shift,
    COUNT(DISTINCT m.id_m) AS total_mothers_in_room
FROM 
    nurse n
JOIN 
    attending_to at ON n.id_n = at.id_n
JOIN 
    room r ON at.id_r = r.id_r
JOIN 
    maternity m ON r.id_r = m.id_r
JOIN 
    birth_record br ON m.id_m = br.id_m
WHERE 
    r.id_r = 10  
    AND EXTRACT(MONTH FROM br.birth_date) = 5 
GROUP BY 
    n.name, n.shift_hours
ORDER BY 
    n.name;






