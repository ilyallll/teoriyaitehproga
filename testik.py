import matplotlib.pyplot as plt
import numpy as np

# Заданные данные
x = np.array([10, 15, 20, 25, 30, 35])
y = np.array([40.202, 36.725, 33.248, 29.771, 26.294, 22.817])

# Уравнения линейной регрессии
eq1 = lambda y: 19.77081 - 0.1689 * y
eq2 = lambda x: (58.14961 - x) / 1.4891

# Построение графика
plt.plot(y, eq1(y), label='x = 19.77081 - 0.1689y')
plt.plot(x, eq2(x), label='y = (58.14961 - x) / 1.4891')

# Вычисление точки пересечения линий
intersection_x = (19.77081 - 58.14961) / (1.4891 + 0.1689)
intersection_y = eq1(intersection_x)
plt.plot(intersection_x, intersection_y, 'ro', label='Intersection')

# Настройка графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики линейных регрессий')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
