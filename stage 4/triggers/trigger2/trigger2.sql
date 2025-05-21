CREATE OR REPLACE FUNCTION reassign_nurse_on_delete()
RETURNS TRIGGER AS $$
DECLARE
  old_shift VARCHAR(15);
  replacement_nurse_id INT;
BEGIN
  -- מצא את המשמרת של האחות שנמחקה
  SELECT shift_hours INTO old_shift
  FROM nurse
  WHERE id_n = OLD.id_n;
  -- מצא אחות אחרת באותה משמרת שאינה האחות שנמחקה, ואינה כבר משויכת לאותו חדר
  SELECT id_n INTO replacement_nurse_id
  FROM nurse
  WHERE shift_hours = old_shift
    AND id_n != OLD.id_n
    AND id_n NOT IN (
      SELECT id_n FROM attending_to WHERE id_r = OLD.id_r)
  ORDER BY RANDOM()
  LIMIT 1;
  -- אם נמצאה אחות מתאימה – קשר אותה לאותו חדר
  IF replacement_nurse_id IS NOT NULL THEN
    INSERT INTO attending_to (id_n, id_r)
    VALUES (replacement_nurse_id, OLD.id_r);
  END IF;
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER reassign_nurse_trigger
AFTER DELETE ON attending_to
FOR EACH ROW
EXECUTE FUNCTION reassign_nurse_on_delete();

DELETE FROM attending_to WHERE id_n = 2166 AND id_r = 348;
select * from attending_to WHERE id_r = 348;