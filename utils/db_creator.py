import json

class TxtData():
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.get_data()

    def update_data(self):
        with open(self.data_path, 'w', encoding='utf-8') as f:
            print(self.data)
            str_data = '\n'.join([str(a) for a in self.data])
            f.write(str_data)
            f.close()

    def get_data(self):
        with open(self.data_path, 'r',
                  encoding='utf-8') as f:
            content = f.read()
            data = [a.strip() for a in content.split('\n')]
            f.close()
        return data

class JsonData():
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.get_data()

    def update_data(self):
        with open(self.data_path, 'w', encoding='utf-8') as f:
            f.write(f'{json.dumps(self.data, ensure_ascii=False, indent=4)}')
            f.close()

    def get_data(self):
        with open(self.data_path, 'r',
                  encoding='utf-8') as f:
            data = json.load(f)
            f.close()
        return data