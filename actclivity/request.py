import urllib.request
import json


def github(username):
    url = f"https://api.github.com/users/{username}/events/public"

    try:
        # Create a request object
        request = urllib.request.Request(url)
        # Add a User-Agent header to avoid 403 error
        request.add_header("User-Agent", "Actclivity")

        # Open the URL and read the response
        with urllib.request.urlopen(request) as response:
            # Parse the response to JSON
            data = json.load(response)
            if data == []:
                return None
            else:
                return data
    except Exception as e:
        print(f"!ERROR: {e}")
        return None
