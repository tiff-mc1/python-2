class TaxMan:
    def __init__(self, items_list, tax):
        self.__total = 0.0
        self.items_list = items_list
        self.tax = tax

    def calc_total(self):
        sum = 0
        for item in self.items_list:
            sum += item['price']
        self.__total = (sum * (int(self.tax[:2]) / 100)) + sum

    def get_total(self):
        return self.__total
