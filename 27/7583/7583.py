from turtle import *

# Открываем файл и считываем данные
f = open('27-2b.txt')

data = []
for line in f:
    s = line.strip().replace(',', '.')  # Убираем лишние символы новой строки
    p = [float(c) for c in s.split()]
    data.append(p)

print("Количество точек:", len(data))


# Функция для вычисления евклидова расстояния между двумя точками
def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# Функция для получения всех точек в пределах радиуса от исходной точки
def get_cluster(p0):
    odin_cluster = [p for p in data if dist(p0, p) < 1]  # Все точки, которые ближе 1 единицы от p0
    if len(odin_cluster) > 0:
        for p in odin_cluster:  # Убираем все точки из data, которые вошли в кластер
            data.remove(p)
    next_cluster = [get_cluster(p) for p in odin_cluster]  # Рекурсивный поиск в кластере
    odin_cluster = odin_cluster + [item for sublist in next_cluster for item in sublist]
    return odin_cluster


clusters = []
while len(data) > 0:
    p0 = data.pop()  # Выбираем точку для начала нового кластера
    cluster = [p0] + get_cluster(p0)  # Создаем кластер, включая найденные точки
    print("Размер кластера:", len(cluster))
    clusters.append(cluster)

print("Общее количество кластеров:", len(clusters))

k = len(clusters)


def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)  # Сумма расстояний до всех других точек
        m.append([s, p])  # Добавляем пару [сумма расстояний, точка]
    return min(m)[1]  # Возвращаем точку, минимизирующую сумму расстояний


# Вычисляем центроиды для каждого кластера
centroid = [center(kl) for kl in clusters]
print("Центроиды кластеров:", centroid)

# Вычисляем сумму координат центроидов
px = sum(x for x, y in centroid)
py = sum(y for x, y in centroid)

print(f"Среднее арифметическое цетров абцис и ординат: {int(px / k * 10000)}, {int(py / k * 10000)}")

# Визуализация разбиения
tracer(0)  # Отключаем автоматическое обновление экрана
colors = ['red', 'green', 'blue'] + ['black'] * (k - 3)  # Цвета для кластеров
screensize(3000, 3000)
# Рисуем каждый кластер разным цветом
for kl, color in zip(clusters, colors):
    up()
    for x, y in kl:
        goto(x * 80, y * 80)  # Масштабируем координаты для визуализации
        dot(3, color)  # Рисуем точку в соответствующем цвете
goto(-100, -100)  # Убираем черепашку
update()  # Обновляем экран после отрисовки всех точек
done()  # Завершаем работу с turtle