CREATE OR REPLACE PROCEDURE assign_mother_to_room(p_childbirth_id INT)
LANGUAGE plpgsql
AS $$
DECLARE
    room_id INT;
BEGIN
    room_id := get_random_free_room();

    IF room_id IS NULL THEN
        RAISE EXCEPTION 'No free rooms with less than 2 mothers available on floors 4 or 5';
    END IF;

    UPDATE maternity
    SET id_r = room_id
    WHERE id_m = p_childbirth_id;

    -- אם עכשיו יש 2 יולדות בחדר, נסמן את החדר כ'לא פנוי'
    IF (SELECT COUNT(*) FROM maternity WHERE id_r = room_id) >= 2 THEN
        UPDATE room SET availability = 'OCCUPIED' WHERE id_r = room_id;
    END IF;

    RAISE NOTICE 'Maternity ID % assigned to room %', p_childbirth_id, room_id;
END;
$$;
