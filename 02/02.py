class Shop:

    total_sales = 0

    def __init__(self, name, goods_sold):
        self._name = name
        self._sales = goods_sold
        Shop.total_sales += goods_sold

    def add_sales(self, qtt):
        self._sales += qtt
        Shop.total_sales += qtt

    def total_sold():
        return f' Всего продано {Shop.total_sales} товаров'

atb = Shop('ATB', 100)
silpo = Shop('Silpo', 50)
novus = Shop('Novus', 30)

print(Shop.total_sold())

silpo.add_sales(25)

print(Shop.total_sold())

