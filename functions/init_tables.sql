CREATE OR REPLACE FUNCTION public.init_tables()
  RETURNS void AS
$$
BEGIN

CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS payment (
    "from" TEXT,
    "to" TEXT,
    "amt" MONEY
);

END
$$
LANGUAGE plpgsql VOLATILE;
