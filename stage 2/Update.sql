UPDATE birth_record 
SET discharge_date = birth_date + 3
WHERE id_br IN (
  SELECT id_br
  FROM birth_record br
  WHERE br.discharge_date != br.birth_date + 3 );

select *
from birth_record;

-----------------------------------------------
UPDATE room
SET availability = 'vacancy';
UPDATE room
SET availability = 'OCCUPIED'
WHERE id_r IN (
  SELECT id_r
  FROM maternity
  GROUP BY id_r
  HAVING COUNT(*) = 2
);

select *
from room;

-----------------------------------------------
UPDATE maternity
SET phone = 57000000 + FLOOR(RANDOM() * 999999)::integer
WHERE id_m = 34;

select *
from maternity
WHERE id_m = 34;

