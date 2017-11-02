-- Test the init_tables() function.

SELECT 'Testing init_tables()' AS "Start";

SELECT 'person-exists' (
    SELECT COUNT(*)
    FROM pg_class pc,
         pg_namespace pn
    WHERE pc.relnamespace = pn.oid
      AND pn.nspname = 'public'
      AND pc.relname = 'person'
) = 1;

SELECT 'person-is-empty', (
    SELECT COUNT(*) FROM person
) = 0;

SELECT 'payment-exists', (
    SELECT COUNT(*)
    FROM pg_class pc,
         pg_namespace pn
    WHERE pc.relnamespace = pn.oid
      AND pn.nspname = 'public'
      AND pc.relname = 'payment'
) = 1;

SELECT 'payment-is-empty', (
    SELECT COUNT(*) FROM payment
) = 0;
