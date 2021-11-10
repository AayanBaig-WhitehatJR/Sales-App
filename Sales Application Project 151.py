# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:47:16 2021

@author: taru_
"""
#basic template tkinter
from tkinter import *
root=Tk()
root.title("Project 151 - Sales Application")
root.geometry("800x600")
root.configure(bg="cyan4")
#c151-tuples code - 
months=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits=("45000", "60000", "80000", "55000", "98000", "99500", "85000", "81000", "95000", "78000", "50000", "35400")
max_profit = max(profits)
print(max_profit)
max_profit_index = profits.index(max_profit)
print(max_profit_index)
max_profit_month = months[max_profit_index]
print("The month earning the most profit is " + str(max_profit_month) + ", having earnt about " + max_profit + ".")

min_profit = min(profits)
print("Minimum profit - " + str(min_profit))
min_profit_index = profits.index(min_profit)
print("Min profit index - " + str(min_profit_index))
min_profit_month = months[min_profit_index]
print("The month earning the least profit is surprisingly " + str(min_profit_month) + ", having earnt only about " + str(min_profit) + " dollars.")
#---------------------code ends here--------------------------
display_month = Label(root)
display_profit = Label(root)
display_max_profit = Label(root)
display_min_profit = Label(root)
#--------------------labels ^^^^^^^^^^^^^^--------------------
display_month["text"]="Months: " + str(months)
display_profit["text"]="Profits: " + str(profits)
#--------------------------------------------------------------------
def find_max_profit():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = months[max_profit_index]
    display_max_profit["text"]="The month earning the most profit is " + str(max_profit_month) + ", having earnt about " + max_profit + "."
def find_min_profit():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = months[min_profit_index]
    display_min_profit["text"]="The month earning the least profit is " + str(min_profit_month) + ", having earnt only about " + min_profit + "." 
#----------------------end code by mainlooping root------------------------
max_button = Button(root, text="Click to show max profit", command=find_max_profit, border="5", bg="steelblue1")
min_button = Button(root, text="Click to show min profit", command=find_min_profit, border="5", bg="steelblue1")
#---------------------------------------------
display_month.place(relx=0.5, rely=0.15, anchor=CENTER)
display_profit.place(relx=0.5, rely=0.25, anchor=CENTER)
max_button.place(relx=0.5, rely=0.35, anchor=CENTER)
display_max_profit.place(relx=0.5, rely=0.45, anchor=CENTER)
min_button.place(relx=0.5, rely=0.55, anchor=CENTER)
display_min_profit.place(relx=0.5, rely=0.65, anchor=CENTER)
root.mainloop()