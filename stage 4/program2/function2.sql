--- function2
CREATE OR REPLACE FUNCTION get_random_department()
RETURNS TABLE(d_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT department_id
    FROM department
    ORDER BY RANDOM()
    LIMIT 1;
END;
$$;

