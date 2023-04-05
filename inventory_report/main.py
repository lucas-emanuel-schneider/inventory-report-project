from inventory_report.inventory.inventory import Inventory
import sys


def main():
    if len(sys.argv) < 3:
        return sys.stderr.write("Verifique os argumentos\n")
    try:
        path = sys.argv[1]
        report_type_method = sys.argv[2]
        report = Inventory.import_data(path, report_type_method)
        sys.stdout.write(report)
    except (ValueError):
        sys.stdout.write("Verifique seus argumentos\n")
