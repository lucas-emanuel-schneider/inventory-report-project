from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if ".csv" not in path:
            raise ValueError("Arquivo com formato inválido!")
        with open(path) as csvfile:
            return list(csv.DictReader(csvfile, delimiter=",", quotechar='"'))
