money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_budget = money_capital + salary  # Бюджет текущего месяца
while current_budget >= spend:
    months += 1
    current_budget -= spend
    spend *= (1 + increase)
    current_budget += salary

print("Количество месяцев, которое можно протянуть без долгов:", months)
