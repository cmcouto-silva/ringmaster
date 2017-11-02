-- Test the wipe_tables() function.

SELECT 'Testing wipe_tables()' AS "Start";

SELECT 'person-doesnt-exist', (
    SELECT COUNT(*)
    FROM pg_namespace pn, pg_class pc
    WHERE pc.relnamespace = pn.oid
      AND pn.nspname = 'public'
      AND pc.relname = 'person'
) = 0;

SELECT 'payment-doesnt-exist', (
    SELECT COUNT(*)
    FROM pg_namespace pn, pg_class pc
    WHERE pc.relnamespace = pn.oid
      AND pn.nspname = 'public'
      AND pc.relname = 'payment'
) = 0;
