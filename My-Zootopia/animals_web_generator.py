import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as fileobj:
    return json.load(fileobj)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    if "name" in animal:
        print("Name:", animal["name"])

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        print('Diet: ',animal["characteristics"]["diet"])

    if "locations" in animal and len(animal["locations"]) > 0:
        print('Location: ',animal["locations"][0])

    if "type" in animal:
        print(animal["type"])
    print()
