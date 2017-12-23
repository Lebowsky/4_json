import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as json_data:
        return json_data.read()    


def pretty_print_json(data):
    try:
        json_data = json.loads(data)
    except ValueError as e:
        print("Не удалось прочитать JSON-файл", e)
        return
    print (json.dumps(json_data, ensure_ascii = False, indent=4, sort_keys=True))


if __name__ == '__main__':
    pretty_print_json(load_data('example.json'))
