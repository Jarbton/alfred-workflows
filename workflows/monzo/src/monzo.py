import os
from sys import stdout, argv


# Get username from Alfred environment variable
username = os.getenv('monzo_username')

# Get input args from Alfred
args = argv[1:]
cost = args[0] # TODO: Validate this is a number

# Generate url with username and cost
url = "https://monzo.me/" + username + "/" + cost

# Try to get reason from args
for index, item in enumerate(args[1:]):
    if not index:
        url += "?d=" + item
    else:
        url += "%20" + item

# Return
stdout.write(url)
