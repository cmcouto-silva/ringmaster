# Setup template taken from learnpythonthehardway.org/book/ex46.html

# Modified on 2015-06-12

# datatools moved from /Users/christie/Gibbs_work/projects/gibbsDB
#                   to /Users/christie/Gibbs_work/projects/packages
#                   on 2015-06-17

def main():
	try:
		from setuptools import setup
	except ImportError:
		from distutils.core import setup

	config = {
		'description': 'Call, document and test functions in a PostgreSQL database',
		'author': 'Matt Christie',
		'download_url': 'https://mj-christie@bitbucket.org/mj-christie/db-driver.git',
		'author_email': 'christiemj09@gmail.com',
		'version': '0.1',
		'install_requires': ['psycopg2-binary', 'sqlalchemy'],
		'packages': ['db_driver'],
		'scripts': [
		    'bin/error',
		    'bin/passed',
		    'bin/failed',
		    'bin/test-checkpoint',
		    'bin/refresh-funcs',
		    'bin/db-driver-init'
		],
		'entry_points': {
		    'console_scripts': [
		        'call=db_driver.call:console_script',
		        'checkpoint=db_driver.checkpoint:console_script',
		        'run=db_driver.run:console_script',
		        'cred=db_driver.cred:console_script',
		        'decs=db_driver.decs:console_script',
		        'get=db_driver.get:console_script',
		        'pause=db_driver.pause:console_script'
		    ]
		},
		'name': 'db-driver'
	}

	setup(**config)	

if __name__ == '__main__':
	main()
