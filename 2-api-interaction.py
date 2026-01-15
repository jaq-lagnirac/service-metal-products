# Justin Caringal
# 
# A script to interact with an API endpoint
# using HTTP requests.
#
# Prompt provided by Service Metal Products

from pprint import pp
import requests

def main() -> None:
    """The main program."""

    URL = 'https://jsonplaceholder.typicode.com/todos'

    ### 1) get the 200 most recent TODOs
    # The preferred way to do it would be to set parameters to sort
    # and limit response, but documentation for the API is not present.
    # Therefore, the most recent 200 will be trimmed in the script.
    # Ex: most_recent_params = {'limit' : 200, 'sort' : 'desc'}
    print('> Executing Part 1.')
    try:
        most_recent_response = requests.get(URL)
        most_recent_response.raise_for_status()
        # assuming IDs are assigned and added to the list
        # chronologically, gets the most recent 200
        mr_item_limit = 200
        mr_data = most_recent_response.json()
        trimmed_data = mr_data[-mr_item_limit:]
        pp(trimmed_data) # prints most recent 200 to standard output

    except requests.exceptions.RequestException as e:
        print(f'An error occured during execution of Part 1.\n{e}')
    print('> Completed Part 1.')


    ### 2) create a TODO
    print('> Executing Part 2.')
    payload = {
        "userId": 1,
        "id": 201,
        "title": "lorem ipsum",
        "completed": False
        }
    
    try:
        create_response = requests.post(URL, data=payload)
        create_response.raise_for_status()
        print('Successfully created TODO.')

    except requests.exceptions.RequestException as e:
        print(f'An error occured during execution of Part 2.\n{e}')
    print('> Completed Part 2.')


    ### 3) delete a TODO given an ID
    print('> Executing Part 3.')
    GIVEN_ID = 41
    delete_target_url = f'{URL}/{GIVEN_ID}'
    try:
        delete_response = requests.delete(delete_target_url)
        delete_response.raise_for_status()
        print(f'Successfully deleted TODO (id: {GIVEN_ID})')

    except requests.exceptions.RequestException as e:
        print(f'An error occured during execution of Part 3.\n{e}')
    print('> Completed Part 3.')


if __name__ == "__main__":
    main()