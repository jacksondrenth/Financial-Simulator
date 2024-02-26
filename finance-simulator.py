import tkinter as tk
import tkinter.ttk as ttk
import random


# functions
# This is to see when a month passes
def check_multiple_of_4():
    global multiple
    if counter % 4 == 0:
        multiple = True
    else:
        multiple = False

# this is made to delete the error window
def delete_error():
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

# this converts your weekly income and splits it into the savings and disposable income
def converter():
    try:
        # clear error entries
        delete_error()
        # get savings rate
        savings_rate = entry_rate.get()
        savings_rate = float(savings_rate)
        # get income
        income = entry_inc.get()
        income = float(income)
        # create savings
        savings = income * savings_rate
        # get previous savings amount
        entry_saves = entry_savings.get()
        entry_saves = float(entry_saves)
        # delete previous savings amount
        entry_savings.delete(0, tk.END)
        # calculate new savings
        new_savings = entry_saves + savings
        # disposable income
        dis_inc = entry_dis_inc.get()
        dis_inc = float(dis_inc)
        dis_inc = income - savings + dis_inc
        # delete disposable income
        entry_dis_inc.delete(0, tk.END)
        new_savings = round(new_savings, 2)
        new_savings = str(new_savings)
        dis_inc = round(dis_inc, 2)
        dis_inc = str(dis_inc)
        # update savings and disposable income
        entry_savings.insert(string=new_savings, index=0)
        entry_dis_inc.insert(string=dis_inc, index=0)
        # counter
        global counter
        counter += 1
        week_count_label.config(text="Week: " + str(counter))
        subtract_weekly()
        check_multiple_of_4()
        subtract_monthly()
    except ValueError:
        entry.insert(string='You must fill all values. (Income, Savings Rate,', index=0)
        entry2.insert(string='Savings, and Disposable Income, Expenses)', index=0)
        entry3.insert(string='or it should be a number', index=0)

# this simulates the summer (when my internship would be)
# I can potential make it so that I can choose any amound of time
def three_month(i=0):
    if i < 12:
        converter()
        root.after(200, three_month, i+1)

# This makes savings and disposable income 0 so you can focus on the button mores
def save_dispo_zero():
    entry_savings.delete(0, tk.END)
    entry_dis_inc.delete(0, tk.END)
    entry_savings.insert(string="0", index=0)
    entry_dis_inc.insert(string="0", index=0)

# this subtracts from disposable with each week
def subtract_weekly():
    food = food_entry.get()
    food = float(food)
    misc = misc_entry.get()
    misc = float(misc)
    total = misc + food
    dis_inc = entry_dis_inc.get()
    dis_inc = float(dis_inc)
    new_dis_inc = dis_inc - total
    new_dis_inc = float(new_dis_inc)
    new_dis_inc = round(new_dis_inc, 2)
    new_dis_inc = str(new_dis_inc)
    entry_dis_inc.delete(0, tk.END)
    entry_dis_inc.insert(string=new_dis_inc, index=0)

# this subtracts from disposable with each month
def subtract_monthly():
    if multiple is True:
        house = housing_entry.get()
        house = float(house)
        car = car_entry.get()
        car = float(car)
        insurance = insurance_entry.get()
        insurance = float(insurance)
        total_month_expense = house + car + insurance
        dis_inc = entry_dis_inc.get()
        dis_inc = float(dis_inc)
        new_dis_inc = dis_inc - total_month_expense
        new_dis_inc = round(new_dis_inc, 2)
        new_dis_inc = str(new_dis_inc)
        entry_dis_inc.delete(0, tk.END)
        entry_dis_inc.insert(string=new_dis_inc, index=0)
    else:
        pass

# this is for a button to simulate a payment that wouldn't be weekly
def expenser():
    try:
        # clear error entries
        delete_error()
        # other stuff
        dis_inc = entry_dis_inc.get()
        dis_inc = float(dis_inc)
        expense = entry_expense.get()
        expense = float(expense)
        dis_inc = dis_inc - expense
        dis_inc = round(dis_inc, 2)
        dis_inc = str(dis_inc)
        entry_dis_inc.delete(0, tk.END)
        entry_dis_inc.insert(string=dis_inc, index=0)
    except ValueError:
        entry.insert(string='You must fill all values.', index=0)
        entry2.insert(string="(Disposable Income & Expense)", index=0)
        entry3.insert(string='or it should be a number', index=0)

# this is to transfer amounts from savings to disposable income
def transfer_savings_to_dispo():
    try:
        # clear error entries
        delete_error()
        # other stuff
        dis_inc = entry_dis_inc.get()
        dis_inc = float(dis_inc)
        savings = entry_savings.get()
        savings = float(savings)
        transfer = entry_save_dispo.get()
        transfer = float(transfer)
        savings = savings - transfer
        dis_inc = dis_inc + transfer
        dis_inc = round(dis_inc, 2)
        savings = round(savings, 2)
        dis_inc = str(dis_inc)
        savings = str(savings)
        entry_savings.delete(0, tk.END)
        entry_savings.insert(string=savings, index=0)
        entry_dis_inc.delete(0, tk.END)
        entry_dis_inc.insert(string=dis_inc, index=0)
    except ValueError:
        entry.insert(string='You must fill all values.', index=0)
        entry2.insert(string="(Transfer Amount to Disposable Income)", index=0)
        entry3.insert(string='or it should be a number', index=0)

# this is the opposite of the previous
def transfer_dispo_to_savings():
    try:
        # clear error entries
        delete_error()
        # other stuff
        dis_inc = entry_dis_inc.get()
        dis_inc = float(dis_inc)
        savings = entry_savings.get()
        savings = float(savings)
        transfer = entry_dispo_save.get()
        transfer = float(transfer)
        savings = savings + transfer
        dis_inc = dis_inc - transfer
        dis_inc = round(dis_inc, 2)
        savings = round(savings, 2)
        dis_inc = str(dis_inc)
        savings = str(savings)
        entry_savings.delete(0, tk.END)
        entry_savings.insert(string=savings, index=0)
        entry_dis_inc.delete(0, tk.END)
        entry_dis_inc.insert(string=dis_inc, index=0)
    except ValueError:
        entry.insert(string='You must fill all values.', index=0)
        entry2.insert(string="(Transfer Amount to Savings)", index=0)
        entry3.insert(string='or it should be a number', index=0)

# this resets the weekly counter
def reset_counter():
    global counter
    counter = 0
    week_count_label.config(text="Week: " + str(counter))

# this clears all entries
def clear_all():
    delete_error()
    entry_dis_inc.delete(0, tk.END)
    entry_savings.delete(0, tk.END)
    entry_expense.delete(0, tk.END)
    entry_save_dispo.delete(0, tk.END)
    entry_dispo_save.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_inc.delete(0, tk.END)
    food_entry.delete(0, tk.END)
    housing_entry.delete(0, tk.END)
    insurance_entry.delete(0, tk.END)
    car_entry.delete(0, tk.END)
    misc_entry.delete(0, tk.END)
    reset_counter()

# this sets random numbers for all expenses and weekly income
def set_random_numbers():
    clear_all()
    ran_inc = round(random.uniform(500,2000), 2)
    ran_inc = str(ran_inc)
    entry_inc.insert(string=ran_inc, index=0)
    ran_rate = round(random.uniform(.01, .5), 2)
    ran_rate = str(ran_rate)
    entry_rate.insert(string=ran_rate, index=0)
    ran_housing = round(random.uniform(400, 3000), 2)
    ran_housing = str(ran_housing)
    housing_entry.insert(string=ran_housing, index=0)
    ran_car = round(random.uniform(20, 200), 2)
    ran_car = str(ran_car)
    car_entry.insert(string=ran_car, index=0)
    ran_ins = round(random.uniform(0, 1000), 2)
    ran_ins = str(ran_ins)
    insurance_entry.insert(string=ran_ins, index=0)
    ran_food = round(random.uniform(100, 300), 2)
    ran_food = str(ran_food)
    food_entry.insert(string=ran_food, index=0)
    ran_misc = round(random.uniform(0, 50), 2)
    ran_misc = str(ran_misc)
    misc_entry.insert(string=ran_misc, index=0)
    save_dispo_zero()


# tkinter window
root = tk.Tk()

root.title("Living Simulator")

# Income
label_inc = ttk.Label(root, text="Income (Weekly)")
label_inc.grid(row=0, column=0, pady=2, padx=75)

entry_inc = ttk.Entry()
entry_inc.grid(row=1, column=0, pady=2)
dollar_sign = ttk.Label(text="$")
dollar_sign.grid(row=1, column=0, sticky="W", padx=20)

# savings rate
label_rate = ttk.Label(text="Savings Rate")
label_rate.grid(row=2, column=0, pady=2)

entry_rate = ttk.Entry()
entry_rate.grid(row=3, column=0, pady=2)
dollar_sign2 = ttk.Label(text="$")
dollar_sign2.grid(row=3, column=0, sticky="W", padx=20)

button_inc = ttk.Button(text="1 Week", command=converter)
button_inc.grid(row=4, column=0, pady=2)

# Expense
label_expense = ttk.Label(root, text="Expense")
label_expense.grid(row=5, column=0, pady=2)

entry_expense = ttk.Entry()
entry_expense.grid(row=6, column=0, pady=2)
dollar_sign4 = ttk.Label(text="$")
dollar_sign4.grid(row=6, column=0, sticky="W", padx=20)

button_expense = ttk.Button(text="Spend", command=expenser)
button_expense.grid(row=7, column=0, pady=2)

# savings
label_savings = ttk.Label(text="Your Savings")
label_savings.grid(row=0, column=1, pady=2)

entry_savings = ttk.Entry()
entry_savings.grid(row=1, column=1, pady=2)
dollar_sign5 = ttk.Label(text="$")
dollar_sign5.grid(row=1, column=1, sticky="W", padx=40)

label_dis_inc = ttk.Label(text="Your Disposable Income")
label_dis_inc.grid(row=2, column=1, pady=2)

entry_dis_inc = ttk.Entry()
entry_dis_inc.grid(row=3, column=1, pady=2)
dollar_sign6 = ttk.Label(text="$")
dollar_sign6.grid(row=3, column=1, sticky="W", padx=40)

# savings to disposable income
label_save_to_dispo = ttk.Label(text="Transfer Amount")
label_save_to_dispo.grid(row=8, column=0, pady=2)

entry_save_dispo = ttk.Entry()
entry_save_dispo.grid(row=9, column=0, pady=2)
dollar_sign7 = ttk.Label(text="$")
dollar_sign7.grid(row=9, column=0, sticky="W", padx=20)

save_to_dispo = ttk.Button(text="To Disposable Income", command=transfer_savings_to_dispo)
save_to_dispo.grid(row=10, column=0, pady=2)

# dispo to savings

entry_dispo_save = ttk.Entry()
entry_dispo_save.grid(row=11, column=0, pady=2)
dollar_sign8 = ttk.Label(text="$")
dollar_sign8.grid(row=11, column=0, sticky="W", padx=20)

dispo_save_button = ttk.Button(text="To Savings", command=transfer_dispo_to_savings)
dispo_save_button.grid(row=12, column=0, pady=2)

# Error message
error_label = ttk.Label(text="Error Message")
error_label.grid(row=9, column=1, pady=2)
entry = ttk.Entry(width=35, font=('Arial'))
entry.grid(row=10, column=1, pady=2)
entry2 = ttk.Entry(width=35, font=('Arial'))
entry2.grid(row=11, column=1, pady=2)
entry3 = ttk.Entry(width=35, font=('Arial'))
entry3.grid(row=12, column=1, pady=2)

# monthly expenses
monthly_label = ttk.Label(text="Monthly Expenses")
monthly_label.grid(row=0, column=2, pady=2, padx=50)


housing_label = ttk.Label(text="Housing Exp. (Total)")
housing_label.grid(row=1, column=2, pady=2)

housing_entry = ttk.Entry()
housing_entry.grid(row=2, column=2, pady=2)
dollar_sign9 = ttk.Label(text="$")
dollar_sign9.grid(row=2, column=2, sticky="W")

car_label = ttk.Label(text="Car Exp. (Total)")
car_label.grid(row=3, column=2, pady=2)

car_entry = ttk.Entry()
car_entry.grid(row=4, column=2, pady=2)
dollar_sign1 = ttk.Label(text="$")
dollar_sign1.grid(row=4, column=2, sticky="W")

insurance_label = ttk.Label(text="Insurance Exp.")
insurance_label.grid(row=5, column=2, pady=2)

insurance_entry = ttk.Entry()
insurance_entry.grid(row=6, column=2, pady=2, sticky="E", padx=10)
dollar_sign10 = ttk.Label(text="$")
dollar_sign10.grid(row=6, column=2, sticky="W")
# weekly expenses
weekly_label = ttk.Label(text="Weekly Expenses")
weekly_label.grid(row=7, column=2, pady=2)

food_label = ttk.Label(text="Food Exp.")
food_label.grid(row=8, column=2, pady=2)

food_entry = ttk.Entry()
food_entry.grid(row=9, column=2, pady=2)
dollar_sign111 = ttk.Label(text="$")
dollar_sign111.grid(row=9, column=2, sticky="W")

misc_label = ttk.Label(text="Misc Exp.")
misc_label.grid(row=10, column=2, pady=2)

misc_entry = ttk.Entry()
misc_entry.grid(row=11, column=2, pady=2)
dollar_sign12 = ttk.Label(text="$")
dollar_sign12.grid(row=11, column=2, sticky="W")

multiple = False
counter = 0
week_count_label = ttk.Label(text="Week: " + str(counter))
week_count_label.grid(row=4, column=1, pady=2)

# reset week
reset_week_button = ttk.Button(text="Reset Week", command=reset_counter)
reset_week_button.grid(row=5, column=1, pady=2, sticky="W", padx=45)

# clear all
clear_all_button = ttk.Button(text="Clear All", command=clear_all)
clear_all_button.grid(row=5, column=1, pady=2, sticky="E", padx=50)

# set random numbers
set_random_button = ttk.Button(text="Set Random Numbers", command=set_random_numbers)
set_random_button.grid(row=6, column=1, pady=2)

# set zero button
set_zero_button = ttk.Button(text="Set Savings & Disposable Income to 0", command=save_dispo_zero)
set_zero_button.grid(row=7, column=1, pady=2)

# three month
three_month_button = ttk.Button(text="Three Month Button", command=three_month)
three_month_button.grid(row=8, column=1, pady=2)

root.mainloop()
