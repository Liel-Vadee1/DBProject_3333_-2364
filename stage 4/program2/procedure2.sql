CREATE OR REPLACE PROCEDURE process_department()
LANGUAGE plpgsql
AS $$
DECLARE
    v_nurse  RECORD;
    v_doctor RECORD;
BEGIN
    -- העלאת שנות ניסיון לכל הרופאים במחלקה ב־1
    UPDATE doctor
    SET seniority = seniority + 1;
    -- עדכון שמות אחיות שמשויכות גם לצוות אונקולוגי באותו תפקיד
    UPDATE nurse n
    SET name = os.full_name
    FROM "OncologyStaff" os
    WHERE n.id_n = os.staff_id
      AND os.role = 'Nurse';
    FOR v_nurse IN SELECT * FROM nurse LOOP
        RAISE NOTICE 'Nurse: %, Shift: %', v_nurse.name, v_nurse.shift_hours;
    END LOOP;
    FOR v_doctor IN SELECT * FROM doctor LOOP
        RAISE NOTICE 'Doctor: %, Seniority: %', v_doctor.name, v_doctor.seniority;
    END LOOP;
EXCEPTION WHEN OTHERS THEN
    RAISE WARNING 'Error in department processing: %', SQLERRM;
END;
$$;