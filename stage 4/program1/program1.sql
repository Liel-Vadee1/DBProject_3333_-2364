CREATE OR REPLACE FUNCTION assign_rooms_and_return()
RETURNS refcursor AS $$
DECLARE
    c_mothers CURSOR FOR
        SELECT m.id_m, m.name, br.delivery_type
        FROM birth_record br
        JOIN maternity m ON br.id_m = m.id_m
        WHERE br.delivery_type = 'C-Section'
          AND (m.id_r IS NULL OR m.id_r NOT IN (
              SELECT id_r FROM room WHERE floor IN (4, 5)));
    mother_rec RECORD;
    ref_cur CONSTANT refcursor := 'refcur';
BEGIN
    CREATE TEMP TABLE temp_results (
        mother_id INT,
        mother_name VARCHAR,
    delivery_type VARCHAR,
        assigned_room INT,
        status TEXT) ON COMMIT DROP;

    OPEN c_mothers;
    LOOP
        FETCH c_mothers INTO mother_rec;
        EXIT WHEN NOT FOUND;

        BEGIN
            CALL assign_mother_to_room(mother_rec.id_m);

            INSERT INTO temp_results VALUES (
                mother_rec.id_m,
                mother_rec.name,
        mother_rec.delivery_type,
                (SELECT id_r FROM maternity WHERE id_m = mother_rec.id_m),
                'Room assigned successfully');

        EXCEPTION WHEN OTHERS THEN
            INSERT INTO temp_results VALUES (
                mother_rec.id_m,
                mother_rec.name,
        mother_rec.delivery_type,
                NULL,
                'Error: ' || SQLERRM);
        END;
    END LOOP;
    CLOSE c_mothers;
    OPEN ref_cur FOR SELECT * FROM temp_results;
    RETURN ref_cur;
END;
$$ LANGUAGE plpgsql;

BEGIN;
SELECT assign_rooms_and_return() AS refcur;
FETCH ALL FROM refcur;
COMMIT;