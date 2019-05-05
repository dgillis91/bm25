import os
import json


def get_config(filename='default') -> dict:
    filename = filename + '.json'
    filepath = os.path.join(
        project_path(), 'config', filename
    )
    with open(filepath, 'r') as config_file:
        cfg = json.loads(config_file.read())
    return cfg


def project_path() -> str:
    return os.path.dirname(
        os.path.split(
            os.path.abspath(__file__)
        )[0]
    )


if __name__ == '__main__':
    # Simple driver test - really should be done with unit.
    print(get_config())
    print(project_path())