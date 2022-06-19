def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2+(y2-y1)**2)**0.5
    return dist

# Тестируем функцию
print(round(distance(2, 4, 2, 9),2))
print(round(distance(12, 8, 12, -9),2))
print(round(distance(23, 0, 15, 32),2))
