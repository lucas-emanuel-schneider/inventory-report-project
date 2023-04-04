from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        1,
        'Coca-cola',
        'Vonpar',
        '04/04/2023',
        '04/04/2030',
        '043234C3203',
        'deixar gelada trincando'
        )
    assert new_product.id == 1
    assert new_product.nome_do_produto == 'Coca-cola'
    assert new_product.nome_da_empresa == 'Vonpar'
    assert new_product.data_de_fabricacao == '04/04/2023'
    assert new_product.data_de_validade == '04/04/2030'
    assert new_product.numero_de_serie == '043234C3203'
    assert new_product.instrucoes_de_armazenamento == 'deixar gelada trincando'
