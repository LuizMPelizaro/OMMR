import json


def get_json(json_filename: str):
    try:
        with open(f"../../input/{json_filename}.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {json_filename} not found")
    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")
    return None
