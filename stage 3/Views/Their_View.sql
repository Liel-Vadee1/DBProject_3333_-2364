--VIEW המציג את המידע על המטופל, אבחנות, תוכניות טיפול ומפגשי טיפול
CREATE VIEW patient_treatment_overview AS
SELECT cp.patient_id, cp.full_name AS patient_name,
    d.diagnosis_id, d.cancer_type, d.diagnosis_date, d.stage,
    tp.plan_id, tp.start_date, tp.end_date, tp.status AS treatment_status,
    ts.session_id, ts.room AS treatment_room, ts.treatment_type
FROM CancerPatient cp
LEFT JOIN Diagnosis d ON cp.patient_id = d.patient_id
LEFT JOIN TreatmentPlan tp ON d.diagnosis_id = tp.diagnosis_id
LEFT JOIN TreatmentSession ts ON tp.plan_id = ts.plan_id;

select * from patient_treatment_overview;
--שאילתה שמחזירה את שמות סוגי המחלות, וכמות האנשים שאובחנו בהם לפני התאריך ה1.1.25
SELECT ptov.cancer_type, COUNT(DISTINCT ptov.patient_id) AS diagnosed_patients_count,
    ptov.diagnosis_date 
FROM patient_treatment_overview ptov
WHERE ptov.diagnosis_date < '2025-01-01'
GROUP BY ptov.cancer_type, ptov.diagnosis_date 
ORDER BY diagnosis_date;
--שהשאילתה מחזירה את שמות החולים וסוגי המחלות שלהם עבור אלו שטופלו ביותר ממפגש טיפול אחד,
--יחד עם מספר מפגשי הטיפול השונים שהם עברו
SELECT  ptov.patient_name, ptov.cancer_type,
    COUNT(DISTINCT ptov.session_id) AS session_count
FROM patient_treatment_overview ptov
GROUP BY ptov.patient_id, ptov.patient_name, ptov.cancer_type
HAVING COUNT(DISTINCT ptov.session_id) > 1
ORDER BY ptov.patient_name;
