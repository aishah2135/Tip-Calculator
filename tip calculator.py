# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:09:10 2024

@author: aisha
"""

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))

print(type(bill))

tip = int(input("What perccentage tip would you like to give? Ex: 15, 20, 25: "))

people = int(input("How many people to split the bill? "))

bill_with_tip = tip / 100 * bill + bill
print (bill_with_tip)

bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amout = "{:.2f}".format(bill_per_person)

print(f"Each person shouldc pay: ${final_amount}")