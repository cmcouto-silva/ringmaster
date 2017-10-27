"""
Fetch the function declarations from a schema of a database.
"""

import json
import os
import sys

import sql


DECS = 'decs/'


class DeclarationSaver(object):
    """Save declarations from a schema in a database."""
    ### TODO: Factor out explicit SQLAlchemy dependencies ###
    
    def __init__(self, schema):
        self.schema = schema
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
        yield from cur
    
    def save(self):
        """Save the function declarations in a preconfigured directory."""
        for name, signature in self.fetch():
            if signature is None:
                signature = []
            with open(os.path.join(DECS, f'{name}.json'), 'w') as file_out:
                json.dump({'name': name, 'signature': signature}, file_out, indent=4)
    

def main(schema):
    """Save the function declarations from a schema in a preconfigured directory."""
    declarations = DeclarationSaver(schema)
    declarations.save()


if __name__ == '__main__':
    main(sys.argv[1])

