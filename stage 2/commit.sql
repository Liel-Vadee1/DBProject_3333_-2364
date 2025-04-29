-- update doctor set name = 'Doctor Cohen' where id_d = 1;
UPDATE doctor
SET name = 'Doctor Cohen'
WHERE id_d = 1;

-- check before commit
SELECT * FROM doctor WHERE id_d = 1;

-- commit the changes 
COMMIT;

-- try to update the name again
UPDATE doctor SET name = 'second try' WHERE id_d = 1;
ROLLBACK;

-- check the name again its need to be still 'Doctor Cohen'
SELECT * FROM doctor WHERE id_d = 1;
