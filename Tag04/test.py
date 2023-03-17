# load json from file
import json

with open('Tag04/generated.json') as f:
    data = json.load(f)
    data['about'] = data['about'].replace('\\\\', '\\')

print(f"about: {data['about']}")
