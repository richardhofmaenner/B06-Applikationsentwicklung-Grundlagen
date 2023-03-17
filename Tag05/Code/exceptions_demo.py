#!/usr/bin/env python3
# coding: utf8

def demo1():
    input_file = open('test.txt', 'r')
    while True: 
        line = input_file.readline()
        if not line: break 
        print(line.rstrip())

def demo2():
    try:
        input_file = open('test.txt', 'r')
        while True: 
            line = input_file.readline()
            if not line: break 
            print(line.rstrip())

    except: # catch all exceptions
        print(f"reading file failed")
       

def demo3():
    try:
        input_file = open('test.txt', 'r')
        while True: 
            line = input_file.readline()
            if not line: break 
            print(line.rstrip())
        return

    except IOError as ioError:
        print(f"reading file failed: {ioError}")
    
    finally:
        if 'input_file' in locals() and input_file:
            input_file.close()

def my_function(number: int):
    if not isinstance(number, int):
        raise TypeError("'number' must be a int")
    if number < 0:
        raise ValueError("'number' must be positive")
    return number + 1

if __name__ == '__main__':
    demo3()

    print("ok up to now")

    #print(my_function(1))   
    #print(my_function("foo bar")) 
    print(my_function(-42))