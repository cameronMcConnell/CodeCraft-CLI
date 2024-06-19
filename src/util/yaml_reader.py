import yaml

class YamlReader:
    def __init__(self, path):
        self.path = path

    def get_yaml_object(self):
        with open(self.path, "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
        return data