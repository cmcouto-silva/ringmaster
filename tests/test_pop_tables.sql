-- Test the pop_tables() function.

SELECT 'Testing pop_tables()' AS "Start";

SELECT 'person-populated-correctly', (
    SELECT COUNT(*)
    FROM person
) = 0;

SELECT 'payment-populated-correctly', (
    SELECT COUNT(*)
    FROM payment
) = 0;
