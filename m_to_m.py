"""
Rename files and directories beginning with M###
to new M### according to user
"""

import os
import re
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

# Initialize variables
pattern = r'(^M)([\d]{3,4})(.*)'


# Request new M number from user
def new_m_nbr():
	new_m = input('Enter new M number: ')
	return new_m


# Recursively search directories for files
def search_dir(directory, new_m):
	# Change path to directory
	os.chdir(directory)
	for file in os.listdir():
		if os.path.isdir(file):
			logging.debug('{} is a directory'.format(file))
			search_dir(file)
		else:
			logging.debug('{} is a file'.format(file))
			result = re.search(pattern, file)
			if result:
				# os.rename(file, new_m)
				logging.debug('{} renamed to {}'.format(file, new_m)


if __name__ == '__main__':
	user_input = new_m_nbr()
	while not(user_input.isnumeric()):
		user_input = new_m_nbr()

	search_dir('.', user_input)
