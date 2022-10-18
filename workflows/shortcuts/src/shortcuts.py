from json import dumps
from subprocess import getoutput
from sys import stdout

# Get shortcuts and split into a list
search_results = getoutput("shortcuts list").splitlines()

# Generate Alfred list
alfred_results = []
for item in search_results:
    # docs: https://www.alfredapp.com/help/workflows/inputs/script-filter/json/
    result = {
        "title": item,
        "subtitle": item,
        "arg": item,
        "autocomplete": item,
        "icon": {"path": "./icon.png"},
        "mods": {"cmd": {"subtitle": f"View {item} in Shortcuts app", "arg": item}},
    }

    alfred_results.append(result)

response = dumps({"items": alfred_results})

stdout.write(response)
