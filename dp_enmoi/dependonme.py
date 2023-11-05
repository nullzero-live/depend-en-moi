from _constants import *
import _libraries
import arg_parser




''' A library designed to initialize required modules for MLOps Tools by Nullzero

Options include:
- WandB
- Langchain
- MLFlow (ToDo)

'''

libraries = ["WandB", "Langchain", "MLFlow"]


import os
import subprocess
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Constants
LOGS_DIR = 'logs'
CACHE_FILE = os.path.join(LOGS_DIR, 'setup_cache.log')
CACHE_DURATION = timedelta(hours=12)

# Function to check if a library is installed and offer to install it


def check_dotenv():
    try:
        # Try to import load_dotenv from dotenv
        from dotenv import load_dotenv, find_dotenv, __version__ as dotenv_version
        
        # Check if the required version is installed
        if dotenv_version == REQUIRED_DOTENV_VERSION:
            return True
        else:
            raise ImportError("Incorrect python-dotenv version installed.")

    except ImportError as e:
        # Attempt to install the correct version of python-dotenv
        print(f"Installing python-dotenv=={REQUIRED_DOTENV_VERSION}...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'python-dotenv=={REQUIRED_DOTENV_VERSION}'])
        # Retry the import after installation
        from dotenv import load_dotenv, find_dotenv
        return True

# Run the check and load .env when module is imported
if check_dotenv():
    load_dotenv(find_dotenv())

def check_library_installed(library_name, AUTO_INSTALL=False):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'show', library_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        if AUTO_INSTALL or (input(f"Do you wish to install {library_name}? (y/n): ").lower() == 'y'):
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', library_name])
            logging
        return f"{library_name} is not installed. Please install it before continuing."




# Function to check for OPENAI_API_KEY and prompt if not found
def check_openai_api_key():
    dotenv.load_dotenv()
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        openai_api_key = input("Enter your OPENAI_API_KEY or 'no' to skip: ").strip()
        if openai_api_key.lower() != 'no':
            with open('.env', 'a') as f:
                f.write(f"OPENAI_API_KEY={openai_api_key}\n")

# Function to run wandb login if WAND* is not in environment
def check_wandb_login():
    dotenv.load_dotenv()
    if not any(key.startswith('WAND') for key in os.environ):
        try:
            import wandb
            wandb.login()
        except ImportError:
            print("wandb is not installed. Please install it before continuing.")

# Function to add .env to .gitignore
def update_gitignore():
    gitignore_path = '.gitignore'
    if not os.path.exists(gitignore_path) or '.env' not in open(gitignore_path).read():
        with open(gitignore_path, 'a') as file:
            file.write('\n# dotenv environment variables file\n.env\n')

# Function to check if setup needs to run based on cache
def is_setup_required():
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)
        return True
    if not os.path.exists(CACHE_FILE):
        return True
    with open(CACHE_FILE, 'r') as file:
        timestamp = datetime.fromisoformat(file.read().strip())
    return datetime.now() > timestamp + CACHE_DURATION

# Function to update the cache timestamp
def update_cache_timestamp():
    with open(CACHE_FILE, 'w') as file:
        file.write(datetime.now().isoformat())

# Main function to run all setup steps
def debug_setup(AUTO_INSTALL=False, DEBUG=False):
    if DEBUG:
        print(f"00x ---- checking dotenv installed ---- x00")
    try: 
        check_dotenv()
        load_dotenv(find_dotenv())
    except Exception as e:
        print(e)

    if check_library_installed('python-dotenv') != True:
    if is_setup_required():
        check_library_installed('python-dotenv', AUTO_INSTALL)
        check_library_installed('wandb', AUTO_INSTALL)
        check_openai_api_key()
        check_wandb_login()
        update_gitignore()
        update_cache_timestamp()
        print("Setup complete.")
    else:
        print("Setup already completed within the last 12 hours.")

# Run setup when module is imported
def main():
run_setup(AUTO_INSTALL=False)







if __name__ == "__main__":
    main()
