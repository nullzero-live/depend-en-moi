import argparse
import os
from contextlib import redirect_stdout

# Create the parser
parser = argparse.ArgumentParser(description="Process some flags.")

# Add the flags to the parser
parser.add_argument('--auto', action='store_true', help='Sets the AUTO_INSTALL variable to True')
parser.add_argument('--debug', action='store_true', help='Sets the DEBUG variable to True')
parser.add_argument('--logging', action='store_true', help='Sets the LOGGING variable to True')
parser.add_argument('-q', '--quiet', action='store_true', help='Suppresses the output')

# Parse the arguments
args = parser.parse_args()

# Set the variables based on the flags
AUTO_INSTALL = args.auto
DEBUG = args.debug
LOGGING = args.logging

# If '-q' or '--quiet' is set, suppress the output
if args.quiet:
    with open(os.devnull, 'w') as f:
        with redirect_stdout(f):
            print('This will not appear anywhere')
    



