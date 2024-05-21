"""
Завдання 1. Оптимізація виробництва

Умови завдання:

"Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
"Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".

Використовуючи PuLP, створіть модель, яка визначає, скільки "Лимонаду" та "Фруктового соку" потрібно виробити
для максимізації загальної кількості продуктів, дотримуючись обмежень на ресурси. Напишіть програму, код якої
максимізує загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.
"""

from pulp import LpMaximize, LpProblem, LpVariable


model = LpProblem("maximize_production", LpMaximize)


x = LpVariable("lemonade", lowBound=0, cat='Integer')  
y = LpVariable("fruit_juice", lowBound=0, cat='Integer') 


model += x + y


model += 2 * x + y <= 100  # water
model += x <= 50  # sugar
model += x <= 30  # lemon juice
model += 2 * y <= 40  # fruit puree


model.solve()


lemonade_prod = x.value()
fruit_juice_prod = y.value()
total_prod = lemonade_prod + fruit_juice_prod

print("Lemonade Production:", lemonade_prod)
print("Fruit Juice Production:", fruit_juice_prod)
print("Total Production:", total_prod)