import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".xml" not in path:
            raise ValueError("Arquivo com formato inválido!")
        with open(path) as xmlfile:
            data = xmltodict.parse(xmlfile.read())
            return data["dataset"]["record"]
