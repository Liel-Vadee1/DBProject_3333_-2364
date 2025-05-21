-- פונקציה שמחזירה חדר פנוי עם פחות מ-2 יולדות, בקומות4 או5 בלבד
CREATE OR REPLACE FUNCTION get_random_free_room()
RETURNS INT AS $$
DECLARE
    room_id INT;
BEGIN
    SELECT id_r
    INTO room_id
    FROM room r
    WHERE r.floor IN (4, 5)
      AND r.availability = 'vacancy'
      AND (SELECT COUNT(*) FROM maternity m WHERE m.id_r = r.id_r) < 2
    ORDER BY RANDOM()
    LIMIT 1;
  
    RETURN room_id;
END;
$$ LANGUAGE plpgsql;
