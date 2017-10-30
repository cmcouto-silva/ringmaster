CREATE OR REPLACE FUNCTION public.pop_tables()
  RETURNS void AS
$$
BEGIN

INSERT INTO person(name) VALUES
    ('Matt Christie'),
    ('Jake Munger'),
    ('Lisa Rausch'),
    ('Dan Fischer'),
    ('Bert Lyons');

INSERT INTO payment("from", "to", "amt") VALUES
    ('Matt Christie', 'Jake Munger', 2.50),
    ('Jake Munger', 'Bert Lyons', 1.75),
    ('Lisa Rausch', 'Bert Lyons', 2.25),
    ('Bert Lyons', 'Dan Fischer', 2.00),
    ('Dan Fischer', 'Jake Munger', 2.25);

END
$$
LANGUAGE plpgsql VOLATILE;
