import json, sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_data:
        try:
            json_data = json.load(json_data)
        except ValueError as e:
            print("Не удалось прочитать JSON-файл", e)
            return
        return json_data


def pretty_print_json(json_data):
    print (json.dumps(json_data, ensure_ascii = False, indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        pretty_print_json(load_data(sys.argv[1]))
