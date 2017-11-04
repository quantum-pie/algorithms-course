# Enumerate .json files in given folder and find in this files object:
# Object have "kind" and "age" fields with arbitrary case
# "kind" is "human" and "age" is greater or equal than 18

import os.path
import json

good_counter = 0
for current_dir, dirs, files in os.walk("data/data"):
    for file in files:
        if file.endswith(".json"):
            with open(current_dir + "/" + file, 'r') as f:
                j_data = json.load(f)
                kind_flag = False
                age_flag = False
                for key in j_data.keys():
                    if key.lower() == "kind" and j_data[key].lower() == "human":
                        kind_flag = True
                    if key.lower() == "age":
                        # try to cast value to integer
                        try:
                            if int(j_data[key]) >= 18:
                                age_flag = True
                        except ValueError:
                            pass
                if kind_flag and age_flag:
                    good_counter += 1

print(good_counter)
