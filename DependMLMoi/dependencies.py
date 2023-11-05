import os
import sys
import subprocess
import pkg_resources
from _constants import *

# Define the path to requirements.txt
REQUIREMENTS_PATH = './requirements.txt'

def upgrade_pip():
    print("Upgrading pip...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

def check_requirements_file():
    if not os.path.isfile(REQUIREMENTS_PATH):
        print(f"The required {REQUIREMENTS_PATH} file is missing.")
        sys.exit(1)
    with open(REQUIREMENTS_PATH, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

def check_packages(required_packages):
    missing_packages = []
    # Check each package to see if it's installed and up to the required version
    for requirement in required_packages:
        try:
            pkg_resources.require(requirement)
        except pkg_resources.DistributionNotFound:
            missing_packages.append(requirement)
        except pkg_resources.VersionConflict:
            installed_version = pkg_resources.get_distribution(requirement.split('==')[0]).version
            missing_packages.append(f"{requirement} (Installed: {installed_version})")
    
    if missing_packages:
        print("The following required packages are missing or not up to the required version:")
        for package in missing_packages:
            print(f" - {package}")
        answer = input("Would you like to automatically install the missing packages? (y/n): ").strip().lower()
        if answer == 'y':
            upgrade_pip()  # Upgrade pip before installing missing packages
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', REQUIREMENTS_PATH])
        else:
            print("\nPlease install or upgrade the missing packages by running:")
            print(f"pip install -r {REQUIREMENTS_PATH}")
            sys.exit(1)
        print(f"{missing_packages} were successfully installed.")
def main_libraries():
    try:
        upgrade_pip()
    except Exception as e:
        print(e)
    # Check for the existence of requirements.txt and read required packages
    required_packages = check_requirements_file()
    # Check for packages when the module is imported
    check_packages(required_packages)
    # Now it's safe to import these packages
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())


