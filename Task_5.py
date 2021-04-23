
# Задание 5

# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


revenue = float(input("Your revenue: "))
expenses = float(input("Your expenses: "))

# total revenue – total expenses = profit
# Return On Sales = (revenue - expenses) / revenue
# Revenue Per Employee = total revenue / current number of employees

profit = revenue - expenses

if profit > 0:
    return_on_sales = profit / revenue
    print(f"\nThat's the spirit!\nYour profit is: {profit:.2f}\nAnd the Return on Sales: {return_on_sales:.2f}")
    curiosity = input("\nDo you want to know the Revenue Per Employee? Yes/No: ")
    if curiosity.lower() == "yes":
        number_emp = int(input("So, how many people do you have employed?: "))
        revenue_emp = revenue / number_emp
        print(f"The Revenue Per Employee: {revenue_emp:.2f}")
    else:
        print(f"That would be \"No\". As you wish")
elif profit == 0:
    print(f"You've lost no money, just time. Your profit is: {int(profit)}")
else:
    print(f"Your profit is: {profit:.2f}\nAnd that's the opposite of profit, my friend")
