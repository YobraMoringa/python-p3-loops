#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i>0:
        if i == 1:
            print(i)
            print("Happy New Year!")
        else:
            print(i)
        i -= 1

def square_integers(int_list):
    # code goes here!
    int_list = [element * element for element in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    for i in range(100):
        i+=1
        if (i%3 == 0 and i%5 == 0):
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
