import json
import os


class JsonFile:
    def __init__(self, file_name):
        self.file_name = os.path.join(self.get_current_path(), 'static', 'data', file_name)

    @staticmethod
    def get_current_path():
        current_path = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.dirname(current_path)
        return path

    def read_json_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def add_data_to_json_file(self, new_data):
        data = self.read_json_file()
        is_new_data = True
        for d in data:
            if d == new_data:
                is_new_data = False
        if is_new_data:
            data.append(new_data)
            self.save_json_file(data)
            return 'Add success'
        else:
            return 'This data is existed'

    def remove_data_from_json_file(self, exist_data):
        data = self.read_json_file()
        is_exist_data = False
        for d in data:
            if d == exist_data:
                is_exist_data = True
        if is_exist_data:
            data.remove(exist_data)
            self.save_json_file(data)
            return 'Remove success'
        else:
            return 'This data is not existed'

    def update_data_on_json_file(self, old_data, new_data):
        data = self.read_json_file()
        is_exist_data = False
        for i in range(len(data)):
            if data[i] == old_data:
                data[i] = new_data
                is_exist_data = True
                self.save_json_file(data)
                return 'Update success'
        if not is_exist_data:
            return 'The old data is not existed'

    def save_json_file(self, data):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    file_names = 'user.json'
    j = JsonFile(file_names)
    print(j.file_name)
