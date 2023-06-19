"""
Install ringmaster.
"""

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Call, document and test functions in a PostgreSQL database',
		'author': 'Matt Christie',
		'download_url': 'https://github.com/christiemj09/ringmaster.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'install_requires': ['psycopg2-binary', 'sqlalchemy'],
		'packages': ['ringmaster'],
		'scripts': [
		    'bin/error',
		    'bin/passed',
		    'bin/failed',
		    'bin/test-checkpoint',
		    'bin/refresh-funcs',
		    'bin/ringmaster-init'
		],
		'entry_points': {
		    'console_scripts': [
		        'call=ringmaster.call:console_script',
		        'checkpoint=ringmaster.checkpoint:console_script',
		        'run=ringmaster.run:console_script',
		        'cred=ringmaster.cred:console_script',
		        'decs=ringmaster.decs:console_script',
		        'get=ringmaster.get:console_script',
		        'pause=ringmaster.pause:console_script',
		        'wait_for=ringmaster.wait_for:console_script',
		    ]
		},
		'name': 'ringmaster'
	}

	setup(**config)	

if __name__ == '__main__':
	main()
