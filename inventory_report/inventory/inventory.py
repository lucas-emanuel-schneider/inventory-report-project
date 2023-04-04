from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read_mode(path):
    if ".csv" in path:
        content = CsvImporter.import_data(path)
    elif ".json" in path:
        content = JsonImporter.import_data(path)
    elif ".xml" in path:
        content = XmlImporter.import_data(path)
    return content


class Inventory:
    @staticmethod
    def import_data(path, type):
        content = read_mode(path)
        if type == "simples":
            return SimpleReport.generate(content)
        elif type == "completo":
            return CompleteReport.generate(content)
