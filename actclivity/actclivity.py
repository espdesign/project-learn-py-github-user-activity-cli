#!/usr/bin/env python
import argparse

# import custom actclivity module
import events
import request

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Echo your input")
    parser.add_argument("username", help="Username to fetch github user activity.")

args = parser.parse_args()

data = request.github(args.username)
try:
    activity = events.Activity(data)
    for event in activity.events:
        print(event)

except TypeError:
    print("Error: Username returned no data, please provide a valid active user")
