CREATE OR REPLACE FUNCTION public.hello_world()
  RETURNS TEXT
  LANGUAGE plpgsql
AS $function$
BEGIN

return 'Hello, world!';

END
$function$
