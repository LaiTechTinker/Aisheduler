#this code block will remove the default generated id from my json file and make it as a normal json file

import json
raw_filepath="./preference_datasets.json"


def remove_id(data):
    if type(data) == dict:
        new_dict = {}

        for key, value in data.items():
            if key != "id" :
                new_dict[key] = remove_id(value)

        return new_dict

    elif type(data) == list:
        return [remove_id(item) for item in data]

    else:
        return data


# Load JSON file
with open(raw_filepath, "r") as f:
    data = json.load(f)

# Remove all "id" fields
cleaned_data = remove_id(data)

# Save result
with open("new_preference.json", "w") as f:
    json.dump(cleaned_data, f, indent=4)

print("Done! All 'id' fields removed.")
