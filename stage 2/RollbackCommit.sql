BEGIN;
UPDATE baby
SET weigt = 3.2 
WHERE id_b = 200;
select *
from baby
where id_b = 200;
ROLLBACK;
END;

--------------------------
BEGIN;
UPDATE doctor
SET seniority = 20 
WHERE id_d = 100;

select *
from doctor
where id_d = 100;

COMMIT;
END;