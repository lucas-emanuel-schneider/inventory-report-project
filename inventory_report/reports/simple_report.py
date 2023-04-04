from datetime import datetime
from collections import Counter


class SimpleReport:

    @classmethod
    def get_oldest_date(cls, list):
        return min(item['data_de_fabricacao'] for item in list)

    @classmethod
    def closest_expiration(cls, list):
        return min([
            item["data_de_validade"] for item in list
            if datetime.strptime(
                item["data_de_validade"], "%Y-%m-%d") > datetime.today()
        ])

    @classmethod
    def get_most_common_company(cls, list):
        return Counter(
            item["nome_da_empresa"] for item in list
            ).most_common(1)[0][0]

    @classmethod
    def generate(cls, list):
        oldest_date = cls.get_oldest_date(list)
        closest_expiration = cls.closest_expiration(list)
        company_with_more_products = cls.get_most_common_company(list)
        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_expiration}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
