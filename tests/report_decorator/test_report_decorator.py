from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    new_product = [
        {
            "id": "1",
            "nome_do_produto": "Coca-cola",
            "nome_da_empresa": "Vonpar",
            "data_de_fabricacao": "2023-04-04",
            "data_de_validade": "2030-04-04",
            "numero_de_serie": "043234C3203",
            "instrucoes_de_armazenamento": "deixar gelada trincando",
        },
    ]
    colored_simple_report = ColoredReport(SimpleReport).generate(new_product)
    colored_complete_report = ColoredReport(
        CompleteReport).generate(new_product)

    assert ("\033[36m" in colored_simple_report) is True
    assert ("\033[36m" in colored_complete_report) is True
    assert ('\099[33m') not in colored_complete_report
    assert ('\099[33m') not in colored_simple_report
