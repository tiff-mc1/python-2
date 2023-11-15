# define your methods here.
# ex1() - ex10()
from WordCounter import WordCounter
from TaxMan import TaxMan
from Calculator import Calculator

people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]


def sort_people(p_list, sort_field, sort_direction):
    res_list = p_list.sort(
        key=lambda p: p[sort_field], reverse=sort_direction == 'desc')
    return res_list


def ex1():
    sort_people(people_list, 'weight', 'desc')
    print(people_list)


def filter_males(p_list):
    return list(filter(lambda p: p['sex'] == 'male', p_list))


def ex2():
    filtered_males = filter_males(people_list)
    print(filtered_males)


def calc_bmi(p_list):
    res = list(
        map(lambda p: {**p, 'bmi': round(p['weight_kg']/p['height_meters'] ** 2, 1)}, p_list))
    return res


def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)


def get_people(p_list):
    res = [p['name'] for p in p_list if p['age'] >= 15]
    return res


def ex4():
    print(get_people(people_list))


def ex5():
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())
    print(word_counter.get_shortest_word())
    print(word_counter.get_longest_word())


def ex6():
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())


def ex7():
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())


if __name__ == '__main__':
    # main()
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    ex7()
