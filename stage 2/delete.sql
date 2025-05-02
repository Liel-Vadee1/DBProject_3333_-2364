SELECT *
FROM birth_record
ORDER BY birth_date ASC;

DELETE FROM midwife
WHERE id_br IN (
  SELECT id_br
  FROM birth_record
  WHERE birth_date < DATE '2025-04-07'
);
DELETE FROM birth_record
WHERE birth_date < DATE '2025-04-07';

------------------------------------------------
SELECT *
FROM doctor
WHERE TRUNC(seniority) = 0
  AND UPPER(birth_specialty) = 'CAESAREAN SECTION';
  
  DELETE FROM midwife
WHERE id_d IN (
  SELECT id_d
  FROM doctor
  WHERE TRUNC(seniority) = 0
  AND UPPER(birth_specialty) = 'CAESAREAN SECTION'
);

delete from doctor
WHERE TRUNC(seniority) = 0
  AND UPPER(birth_specialty) = 'CAESAREAN SECTION';

------------------------------------------------
select *
from nurse
where id_n not in (select id_n from attending_to);

delete from nurse
where id_n not in (select id_n from attending_to);
