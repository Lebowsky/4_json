import json
import sys


def load_data(file_path):
    with open(file_path, encoding='utf-8') as json_data:
        json_data = json.load(json_data)
        return json_data


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            json_data = load_data(sys.argv[1])
        except (FileNotFoundError, ValueError) as e:
            print("Не удалось прочитать JSON-файл", e)
        else:
            pretty_print_json(json_data)
