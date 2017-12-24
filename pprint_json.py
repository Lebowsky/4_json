import json, sys


def load_data(file_path):
    with open(file_path, encoding='utf-8') as f:
        return f.read()


def json_parse(json_text):
    try:
        json_data = json.loads(json_text)
    except ValueError as e:
        print("Не удалось прочитать JSON-файл", e)
        return
    return json_data


def pretty_print_json(json_data):
    print (json.dumps(json_data, ensure_ascii = False, indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        json_text = load_data(sys.argv[1])
        json_data = json_parse(json_text)
        pretty_print_json(json_data)
