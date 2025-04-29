-- stage 1: update 
UPDATE room
SET availability = 'in use'
WHERE floor = 2;

-- stage 2: check values after update
SELECT * FROM room WHERE floor = 2;

-- stage 3: ROLLBACK
ROLLBACK;

-- stage 4: check values after rollback 
SELECT * FROM room WHERE floor = 2;
