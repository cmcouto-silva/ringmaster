"""
Run a function from a JSON configuration file.
"""

import inspect
import json
import os


def from_config(func):
	"""Run a function from a JSON configuration file."""
	
	def decorator(filename):
		with open(filename, 'r') as file_in:
			config = json.load(file_in)
		return func(**config)
	
	return decorator


def from_json(func):
	"""Run a function from a JSON configuration file."""
	# Mirror of from_config; keeping the original for compatibility reasons
	
	def decorator(filename):
		with open(filename, 'r') as file_in:
			config = json.load(file_in)
		return func(**config)
	
	return decorator


def from_env(func):
    """Run a function from a set of environment variables."""
    
    def decorator():
        params = {
            param.name: os.environ[param.name]
            for param in inspect.signature(func).parameters.values()
            if param.kind not in [param.VAR_POSITIONAL, param.VAR_KEYWORD]
            # ^^ i.e. not *args or **kwargs
        }
        return func(**params)
    
    return decorator
