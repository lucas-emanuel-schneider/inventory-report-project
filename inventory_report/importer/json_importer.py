from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".json" not in path:
            raise ValueError("Arquivo com formato inválido!")
        with open(path) as jsonfile:
            return json.load(jsonfile)
