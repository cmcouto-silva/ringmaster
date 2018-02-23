CREATE OR REPLACE FUNCTION public.pop_tables()
  RETURNS void AS
$$
BEGIN

INSERT INTO person(name) VALUES
    ('Paul McCartney'),
    ('John Lennon'),
    ('George Harrison'),
    ('Ringo Starr'),
    ('Brian Epstein');

INSERT INTO payment("from", "to", "amt") VALUES
    ('Paul McCartney', 'John Lennon', 2.50),
    ('John Lennon', 'Ringo Starr', 1.75),
    ('George Harrison', 'Ringo Starr', 2.25),
    ('Ringo Starr', 'Brian Epstein', 2.00),
    ('Brian Epstein', 'John Lennon', 2.25);

END
$$
LANGUAGE plpgsql VOLATILE;
