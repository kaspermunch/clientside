import requests

# Replace 'YOUR_API_KEY' with your CurseForge API key
api_key = 'YOUR_API_KEY'

def get_mod_name_from_project_id(project_id):
    # Replace 'YOUR_API_KEY' with your CurseForge API key
    api_key = 'YOUR_API_KEY'

    # URL for the CurseForge API to get mod details by project ID
    api_url = f'https://api.cfwidget.com/minecraft/mc-mods/{project_id}?apiKey={api_key}'

    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            mod_info = response.json()
            
            # Extract and return the mod name
            if 'name' in mod_info:
                return mod_info['name']

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Return None if the mod name couldn't be retrieved
    return None


def get_curseforge_mod_id(mod_name):

    # URL for the CurseForge API mod search
    api_url = f'https://api.cfwidget.com/minecraft/mc-mods/search?game=minecraft&query={mod_name}&pageSize=1&apiKey={api_key}'

    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            mod_data = response.json()

            # Check if any mods were found
            if 'data' in mod_data and len(mod_data['data']) > 0:
                first_mod = mod_data['data'][0]

                # Extract and return the mod ID
                return first_mod['id']

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Return None if no mod was found
    return None


# Function to check if a CurseForge mod is client-side
def is_client_side_mod(mod_id):

    # URL for the CurseForge API
    api_url = f'https://api.cfwidget.com/minecraft/mc-mods/{mod_id}?apiKey={api_key}'

    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            mod_info = response.json()

            # Check if the mod has any files
            if 'latestFiles' in mod_info and len(mod_info['latestFiles']) > 0:
                latest_file = mod_info['latestFiles'][0]

                # Check if the latest file is for the client-side
                if 'gameVersion' in latest_file and 'client' in latest_file['gameVersion']:
                    return True

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return False


# Replace 'YOUR_PROJECT_ID' with the project ID of the mod you want to get the name for
project_id = 'YOUR_PROJECT_ID'

mod_name = get_mod_name_from_project_id(project_id)

# Replace 'YOUR_MOD_NAME' with the name of the mod you want to find the ID for
mod_name = 'YOUR_MOD_NAME'

mod_id = get_curseforge_mod_id(mod_name)

assert mod_id is not None
# if mod_id:
#     print(f"The CurseForge ID for the mod '{mod_name}' is: {mod_id}")
# else:
#     print(f"No mod with the name '{mod_name}' was found on CurseForge.")

import sys
mod_id = sys.argv[1]

if is_client_side_mod(mod_id):
    print(f"The mod with ID {mod_id} is client-side.")
else:
    print(f"The mod with ID {mod_id} is not client-side.")

