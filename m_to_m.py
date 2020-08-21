"""
Rename files and directories beginning with M###
to new M### according to user
"""

import os
import re
import logging


# Uncomment to display logging
logging.basicConfig(level=logging.DEBUG)

# Initialize variables
pattern = r'(^M)([\d]{3,4})(.*)'
directory = '.git'


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
            # search_dir(file, new_m)
        else:
            logging.debug('{} is a file'.format(file))
            result = re.search(pattern, file)
            if result:
                new_name = 'M' + str(new_m) + result[3]
                # os.rename(file, new_name)
                logging.debug('{} renamed to {}'.format(file, new_name))


if __name__ == '__main__':
    user_input = new_m_nbr()
    while not (user_input.isnumeric()):
        user_input = new_m_nbr()

    search_dir(directory, user_input)
