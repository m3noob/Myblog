```
import requests

GITLAB_URL = "https://gitlab.sajitta.my.id/api/v4"
PRIVATE_TOKEN = "glpat-9mS4JzaEPAFFrj56XBkm"

user_ids = [16, 17, 18]

counter = 1
for user_id in user_ids:
    delete_user_url = f"{GITLAB_URL}/users/{user_id}"

    headers = {"PRIVATE-TOKEN": PRIVATE_TOKEN}
    response = requests.delete(delete_user_url, headers=headers)

    if response.status_code == 204:
        print("-" * 40)
        print(f"{counter}. User ID: {user_id}")
        print(f"User with ID {user_id} deleted successfully.")
        counter += 1

        print("-" * 40)
        print("")

    elif response.status_code == 404:
        print(f"User with ID {user_id} not found. Unable to delete.")
    else:
        print(f"Failed to delete user with ID {user_id}. Status code: {response.status_code}")
        print(response.text)
```
