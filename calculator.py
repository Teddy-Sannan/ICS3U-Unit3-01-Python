#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: September 2019
# This program adds two numbers together


def main():
    # this program adds two numbers together
    # input
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))
    # process
    calculation = first_number + second_number
    # output
    print("")
    print(first_number, "+", second_number, "=", calculation)


if __name__ == "__main__":
    main()
