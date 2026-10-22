import math

def add_two_numbers():
    num1 = 2
    num2 = 3
    sum = num1 + num2
    return sum
print(add_two_numbers())

def area_of_circle():
    r = 2
    PI = 3.14
    area = PI * r * r
    return area
print(area_of_circle())

def add_all_nums(*args):
    total = 0
    for x in args :
        total += x
    return total
print(add_all_nums(2,3,4,5,7,9,7,2,1))

def convert_celsius_to_fahrenheit(*args):
    F =0
    for C in args :
        F =(C * 9/5 ) + 32
    return F
print(convert_celsius_to_fahrenheit(30))

def check_season(mounth):
    if mounth == 12 or mounth == 1 or mounth == 2 :
        return "Winter"
    elif mounth == 3 or mounth == 4 or mounth == 5 :
        return "Spring"
    elif mounth == 8 or mounth == 7 or mounth == 6 :
        return "Summer"
    elif mounth == 9 or mounth == 10 or mounth == 11 :
        return "Autumn"
print(check_season(1))

def calculate_slope(x1,y1 ,x2,y2):
    if x1 == x2 :
        return None
    else :
        slope = (y2 -y1) / (x2 -x1)
        return slope
print(calculate_slope(4,3,4,2))

def solve_quadratic_eqn(a,b,c):
    Delta = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(Delta)) / (2 * a)
    x2 = (-b - math.sqrt(Delta)) / (2 * a)
    if Delta == 0 :
        return Delta == -b / (2 * a)
    elif Delta > 0 :
        return x1 and x2
    elif Delta < 0 :
        print("Ensemble vide")
print(solve_quadratic_eqn(4,5,6))

def print_list(list):
    for number in list :
        print(number)
print_list([1,2,3])


def reverse_list(items):
    result = []
    for num in items:
        result.insert(0,num)
    return result
print(reverse_list([1,2,3,4]))  




food_stuff = ['Potato','Tomato','Mango','Milk']
def add_item(items,item):
    items.append(item)
    return items
print(add_item(food_stuff,'Meat'))


def sum_of_numbers(n):
    total =0
    for x in range(1,n+1):
        total+=x
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))   
print(sum_of_numbers(100)) 

def sum_of_odds(n):
    total =0
    for x in range(1,n+1):
        if x % 2 == 1:
            total+=x
    return total
print(sum_of_odds(2))


def sum_of_even(n):
    total =0
    for x in range(1,n+2):
        if x % 2 == 0:
            total+=x
    return total
print(sum_of_even(2))

