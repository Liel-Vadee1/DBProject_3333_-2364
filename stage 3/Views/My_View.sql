--VIEW המציג את פרטי האימהות, התינוקות, הלידות והרופאים המיילדים
CREATE VIEW mothers_births_info AS
SELECT m.id_m, m.name AS mother_name, m.age AS mother_age,
    m.phone AS mother_phone, br.id_br, br.birth_date, br.discharge_date,
    br.delivery_type, b.id_b, b.weigt AS baby_weight, b.gender AS baby_gender,
    d.id_d, d.name AS doctor_name
FROM birth_record br
JOIN maternity m ON br.id_m = m.id_m
JOIN baby b ON br.id_b = b.id_b
LEFT JOIN midwife mw ON br.id_br = mw.id_br
LEFT JOIN doctor d ON mw.id_d = d.id_d;

select * from mothers_births_info;
--מחזיר את שמות האימהות והתינוקות שלהם לאלו שטופלו על ידי יותר מאחות אחת
SELECT mbi.id_m AS mother_id, mbi.mother_name, mbi.id_b AS baby_id
FROM mothers_births_info mbi
WHERE mbi.id_m IN (SELECT m.id_m
    FROM maternity m
    JOIN room r ON m.id_r = r.id_r
    JOIN attending_to at ON r.id_r = at.id_r
    GROUP BY m.id_m
    HAVING COUNT(DISTINCT at.id_n) > 1)
ORDER BY mbi.id_m;
--מחזיר את שמות הרופאים, האחיות המטפלים באמהות שילדו לפני התאריך 5.5.25
SELECT DISTINCT mbi.doctor_name, n.name AS nurse_name, mbi.mother_name, 
mbi.birth_date
FROM mothers_births_info mbi
JOIN maternity m ON mbi.id_m = m.id_m
JOIN room r ON m.id_r = r.id_r
JOIN attending_to at ON r.id_r = at.id_r
JOIN nurse n ON at.id_n = n.id_n
WHERE mbi.birth_date < '2025-05-05'
ORDER BY mbi.mother_name, mbi.birth_date, mbi.doctor_name, n.name;