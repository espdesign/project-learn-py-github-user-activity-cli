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
            return data

    except urllib.error.HTTPError as e:
        print(f"HTTP error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
    except Exception as e:
        print(f"An error occurred: {e}")
