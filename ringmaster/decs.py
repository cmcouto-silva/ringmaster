"""
Fetch the function declarations from a schema of a database.
"""

import json
import os
import sys

from ringmaster import sql


DECS = '.decs/'


class DeclarationSaver(object):
    """Save function declarations from a schema in a database."""
    
    def __init__(self, schema, location=DECS):
        self.schema = schema
        self.location = location
        self.conn = sql.preconfigured_connection()
    
    def fetch(self):
        """Fetch function declarations from the database schema."""
        cur = self.conn.cursor()
        cur.execute("""
        SELECT pg_proc.proname, pg_proc.proargnames
        FROM pg_proc, pg_namespace
        WHERE pg_proc.pronamespace = pg_namespace.oid
          AND pg_namespace.nspname = %s
        ORDER BY pg_proc.proname;
        """, (self.schema,))
        return cur
    
    def save(self):
        """Save the function declarations in a preconfigured directory."""
        for name, signature in self.fetch():
            if signature is None:
                signature = []
            filename = os.path.join(self.location, '{name}.json'.format(name=name))
            with open(filename, 'w') as file_out:
                json.dump({'name': name, 'signature': signature}, file_out, indent=4)
    

def main(schema, location=DECS):
    """Save the function declarations from a schema in a preconfigured directory."""
    declarations = DeclarationSaver(schema, location=location)
    declarations.save()


def console_script():
    main(*sys.argv[1:])


if __name__ == '__main__':
    console_script()
