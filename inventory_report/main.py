# from inventory_report.importer.xml_importer import XmlImporter
# from inventory_report.importer.csv_importer import CsvImporter
# from inventory_report.importer.json_importer import JsonImporter
# from inventory_report.inventory.inventory_refactor import InventoryRefactor
# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport

# import sys


# def get_report_type(type, result):
#     if type == "simples":
#         sys.stdout.write(SimpleReport.generate(result))
#     else:
#         sys.stdout.write(CompleteReport.generate(result))


# def main():
#     if len(sys.argv) < 3:
#         return sys.stderr.write("Verifique os argumentos\n")
#     path = sys.argv[1]
#     report_type_method = sys.argv[2]
#     if path.endswith(".csv"):
#         importer = CsvImporter()
#     elif path.endswith(".json"):
#         importer = JsonImporter()
#     elif path.endswith(".xml"):
#         importer = XmlImporter()
#     else:
#         return sys.stderr.write("Arquivo não suportado!\n")
#     data = InventoryRefactor(importer)
#     result = data.import_data(path, report_type_method)
#     get_report_type(report_type_method, result)
