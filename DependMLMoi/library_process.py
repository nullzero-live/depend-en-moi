from constants import CUSTOM
from liblist import supported_libraries
import requests
import toml
from termcolor import colored

def fetch_latest_version(library):
    """Fetch the latest version of a library from PyPI."""
    url = f"https://pypi.org/pypi/{library}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        return data['info']['version']
    except requests.exceptions.HTTPError as http_err:
        print(colored(f"HTTP error occurred: {http_err}", 'red', attrs=['bold']))
    except Exception as err:
        print(colored(f"An error occurred: {err}", 'red', attrs=['bold']))
    return None

def process_libraries(library_list):
    """
    Process a list of Python libraries to extract their latest versions
    and save them to a TOML configuration file.
    """
    library_versions = {}

    for library in library_list:
        latest_version = fetch_latest_version(library)
        if latest_version:
            library_versions[library] = latest_version
            print(colored(f"Latest version of {library} is {latest_version}", 'green', attrs=['bold']))
        else:
            print(colored(f"Could not fetch the latest version for {library}", 'yellow', attrs=['bold']))

    # Write to TOML file
    with open('libraries.toml', 'w') as toml_file:
        toml.dump({'libraries': library_versions}, toml_file)
    print(colored("Configuration has been written to libraries.toml", 'green', attrs=['bold']))

# Example usage
libraries_to_process = supported_libraries.append(CUSTOM)
process_libraries(libraries_to_process)
