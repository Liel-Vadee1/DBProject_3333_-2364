CREATE OR REPLACE FUNCTION get_department_summary()
RETURNS refcursor AS $$
DECLARE
    v_dept RECORD;
    ref_cur refcursor;
BEGIN
    OPEN ref_cur FOR SELECT 'placeholder';
    CLOSE ref_cur;
    SELECT * INTO v_dept FROM get_random_department();
    RAISE NOTICE 'Selected department ID: %', v_dept.d_id;
    ref_cur := 'refcur';
    IF v_dept.d_id = 7 THEN
        CALL process_department();
        OPEN ref_cur FOR
        SELECT 
            d.name AS doctor_name,
            COUNT(br.id_br) AS birth_count
        FROM doctor d
        JOIN midwife mw ON d.id_d = mw.id_d
        JOIN birth_record br ON br.id_br = mw.id_br
        WHERE d.department_id = 7
          AND br.birth_date >= CURRENT_DATE - INTERVAL '1 year'
        GROUP BY d.name;
    ELSE
        OPEN ref_cur FOR
        SELECT 
            dg.cancer_type AS diagnosis,
            COUNT(DISTINCT cp.patient_id) AS patient_count,
            ROUND(AVG(EXTRACT(YEAR FROM AGE(CURRENT_DATE, cp.birth_date))), 1) AS avg_patient_age,
            COUNT(tp.plan_id) AS planned_treatment_count
        FROM cancerpatient cp
        JOIN diagnosis dg ON cp.patient_id = dg.patient_id
        JOIN treatmentplan tp ON dg.diagnosis_id = tp.diagnosis_id
        JOIN oncologystaff os ON dg.staff_id = os.staff_id
        WHERE os.department_id = v_dept.d_id
          AND tp.status = 'Planned'
        GROUP BY dg.cancer_type;
    END IF;
    RETURN ref_cur;
EXCEPTION
    WHEN OTHERS THEN
        RAISE WARNING 'Unexpected error: %', SQLERRM;
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;
BEGIN;
SELECT get_department_summary() INTO refcur;
FETCH ALL FROM refcur;
COMMIT;