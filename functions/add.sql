CREATE OR REPLACE FUNCTION public.add(x INTEGER, y INTEGER)
  RETURNS INTEGER
  LANGUAGE plpgsql
AS $function$
BEGIN

return x + y;

END
$function$
