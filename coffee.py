from class_decorator import MilkCoffee, Syrup, Sugar, CountCalls
from function_decorator import milk_coffee, syrup, sugar, count_calls


@CountCalls
@MilkCoffee
@Syrup('Mapple')
@Sugar(2)
def coffee(type_of_coffee):
    """Coffee Function"""
    print(f'Making Coffee {type_of_coffee}....')
    print('Coffee')


@count_calls
@sugar(2)
@syrup('Maple')
@milk_coffee
def another_coffee(type_of_coffee):
    print(f'Making Another Cofee: {type_of_coffee} ....')
    print('Coffee')


if __name__ == '__main__':
    for coffe_type in ('Cappuccino', 'Espresso', 'Frapuccino'):
        coffee(coffe_type)
    another_coffee('Latte')

    print(f'function coffee called {coffee.calls_count} times')
    print(f'function another_coffee called {another_coffee.calls_count} times')
