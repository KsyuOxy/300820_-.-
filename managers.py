from drivers import JSONDriver


class GoodsManager(JSONDriver):  # ->
    def __init__(self, path='goods.json'):
        super().__init__(path)

    def add_goods(self, goods: dict):  # ->
        goods_dict = self.load_data()
        print(goods_dict)
        names = [i['name'] for i in goods_dict['goods']]  # ->

        tare = [i['tare'] for i in goods_dict['goods']]   # ->

        if goods['name'] not in names and goods['tare'] not in tare:  # ->
            goods_dict['goods'].append(goods)  # ->
        else:
            print('Warning')
        self.save_data(goods_dict)  # ->

    def delete_goods(self, name: str, tare: str):  # ->
        goods_dict = self.load_data()

        for i, goods in enumerate(goods_dict['goods']):          # ->
            if goods['name'] == name and goods['tare'] == tare:  # ->
                removed_el = goods_dict['goods'].pop(i)          # ->
                break
        self.save_data(goods_dict)  # ->

    def get_goods(self, name: str):  # ->
        goods_dict = self.load_data()

        for i, el in enumerate(goods_dict['goods']):  # ->
            print(goods_dict['goods'])
            print(el)
            if el['name'] == name:                    # ->
                return el

    def group_by_tare(self, tare: float) -> list:  # -> отбирает в список товары по таре
        goods_dict = self.load_data()
        list_goods = []  # ->

        for el in goods_dict['goods']:  # ->
            if el.get('tare') == tare:  # ->
                list_goods.append(el)   # ->
        # print(list_goods)
        return list_goods


class CategoriesManager(JSONDriver):  # ->
    def __init__(self, path='categories.json'):
        super().__init__(path)

    def delete_category(self, category: str):  # ->
        categories_dict = self.load_data()

        for i, cat in enumerate(categories_dict['categories']):  # ->
            if cat['category'] == category:  # ->
                removed_el = categories_dict['categories'].pop(i)  # ->
                break
        self.save_data(categories_dict)

    def add_category(self, category: dict):  # ->
        categories_dict = self.load_data()

        list_categories = [i['category'] for i in categories_dict['categories']]  # ->
        list_producers = [i['producer'] for i in categories_dict['categories']]  # ->

        if category['category'] not in list_categories or category['producer'] not in list_producers:
            categories_dict['categories'].append(category)  # ->
        else:
            print('Warning')
        self.save_data(categories_dict)

    def get_categories(self) -> set:  # -> возвращает все виды категорий товаров
        categories_dict = self.load_data()
        set_categories = set()  # ->
        for el in categories_dict['categories']:  # ->
            set_categories.add(el['category'])  # ->
        # print(set_categories)
        return set_categories

    def get_producers(self):  # -> возвращает всех производителей товаров
        categories_dict = self.load_data()
        set_producers = set()  # ->
        for el in categories_dict['categories']:  # ->
            set_producers.add(el['producer'])  # ->
        # print(set_producers)
        return set_producers


class DataManager(GoodsManager, CategoriesManager):  # ->
    def __init__(self, path1='goods.json', path2='categories.json'):
        # GoodsManager.__init__(self, path1)
        CategoriesManager.__init__(self, path2)
        GoodsManager.__init__(self, path1)
        self._path1 = path1
        self._path2 = path2

    def categgoods(self, category: str):  # -> формирует список производителей и товаров по категории

        goods_dict = GoodsManager().load_data()  # -> получает данные из 'goods.json'
        category_dict = CategoriesManager().load_data()  # -> получает данные из 'categories.json'

        category_goods = {category + ' producers': [], 'goods': []}  # ->

        for i in category_dict['categories']:  # ->
            if i['category'] == category:      # ->
                category_goods[category + ' producers'].append(i['producer'])

        if category == 'beverages':  # ->
            [category_goods['goods'].append(i) for i in goods_dict['goods'] if 'tare' in i]

        elif category == 'tea':  # ->
            [category_goods['goods'].append(i) for i in goods_dict['goods'] if i.get('tare') == 0.2]

        elif category == 'baking':  # ->
            [category_goods['goods'].append(i) for i in goods_dict['goods'] if i.get('tare') == 0]
        print(category_goods)

    def get_all(self, name: str):
        goods_dict = GoodsManager().load_data()  # -> получает данные из 'goods.json'
        category_dict = CategoriesManager().load_data()  # -> получает данные из 'categories.json'
        if goods_dict.delete_goods():
            pass
