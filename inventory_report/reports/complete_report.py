from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @classmethod
    def get_all_companys_and_nr_products(cls, list):
        companys = dict()
        for item in list:
            if item['nome_da_empresa'] not in companys:
                companys[item['nome_da_empresa']] = 0
            companys[item['nome_da_empresa']] += 1
        result = ''
        for item in companys.items():
            print(item)
            result += f"- {item[0]}: {item[1]}\n"
        return result

    @classmethod
    def generate(cls, list):
        oldest = cls.get_oldest_date(list)
        closest_expiration = cls.closest_expiration(list)
        company_with_more_products = cls.get_most_common_company(list)
        all_companys_and_items = cls.get_all_companys_and_nr_products(list)
        return (
            f"""Data de fabricação mais antiga: {oldest}
Data de validade mais próxima: {closest_expiration}
Empresa com mais produtos: {company_with_more_products}
Produtos estocados por empresa:\n{all_companys_and_items}"""
        )
