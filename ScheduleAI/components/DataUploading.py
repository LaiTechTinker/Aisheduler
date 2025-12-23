import os
import json
from dotenv import load_dotenv
from ScheduleAI.utils.mongodb import MongoDBOp
raw_filepath="./raw_documents.json"
data=json.load(raw_filepath)

def remove_id(data):
    if type(data) == dict:
        new_dict = {}

        for key, value in data.items():
            if key != "id":
                new_dict[key] = remove_id(value)

        return new_dict

    elif type(data) == list:
        return [remove_id(item) for item in data]

    else:
        return data


# Load JSON file
with open(data, "r") as f:
    data = json.load(f)

# Remove all "id" fields
cleaned_data = remove_id(data)

# Save result
with open("new_raw.json", "w") as f:
    json.dump(cleaned_data, f, indent=4)

print("Done! All 'id' fields removed.")
