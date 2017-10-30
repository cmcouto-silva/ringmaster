-- Get info on the indexes in the database.

CREATE VIEW mattc.index_info AS
    SELECT pn.nspname AS schema_name,
           pc2.relname AS rel_name,
           pc1.relname AS index_name,
           pi.indisprimary::INT AS index_is_primary,
           pg_get_indexdef(pi.indexrelid, 0, TRUE) AS index_def
    FROM pg_namespace pn,
         pg_index pi,
         pg_class pc1,
         pg_class pc2
    WHERE pn.oid = pc2.relnamespace
      AND pc2.oid = pi.indrelid
      AND pc1.oid = pi.indexrelid;
