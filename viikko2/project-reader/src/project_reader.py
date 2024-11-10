from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):

        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)

        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]
        license = data["tool"]["poetry"].get("license", "-")
        authors = data["tool"]["poetry"].get("authors", [])
        dependencies = list(data["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(data["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())

        return Project(name, description, dependencies, dev_dependencies, license, authors)
