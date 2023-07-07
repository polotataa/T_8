import math
# class Point:
#     latitude: float
#     longitude: float
# class Road:
#     start_point: Point
#     end_point: Point


#Класс, определяющий географические координаты точки (широту и долготу)
class Point:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


#Класс, определяющий дорогу между двумя точками (начальная и конечная точка)
class Road:
    def __init__(self, start_point: Point, end_point: Point):
        self.start_point = start_point
        self.end_point = end_point


#Функция, которая возвращает истину в случае существованиятакого маршрута.
def route_exist(road_1: Road, road_2: Road) -> bool:
    # Расчет расстояния между точками в километрах
    def calculate_distance(point1: Point, point2: Point) -> float:
        # Преобразование географических координат в радианы
        lat1 = math.radians(point1.latitude)
        lon1 = math.radians(point1.longitude)
        lat2 = math.radians(point2.latitude)
        lon2 = math.radians(point2.longitude)

        # Расчет разницы между координатами
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        # Формула гаверсинусов для расчета расстояния на сфере
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        # Расстояние в километрах
        distance = 6371 * c
        return distance

    # Проверка наличия маршрута между точками
    distance = calculate_distance(road_1.end_point, road_2.start_point)
    if distance <= 100:  # Предположим, что максимальное расстояние между точками, чтобы считать маршрут возможным, равно 100 км
        return True
    else:
        return False


# Создание экземпляров класса Point
point1 = Point(latitude=51.5074, longitude=-0.1278)  # Лондон
point2 = Point(latitude=40.7128, longitude=-74.0060)  # Нью-Йорк

# Создание экземпляров класса Road
road1 = Road(start_point=point1, end_point=point2)
road2 = Road(start_point=point2, end_point=point1)

print(route_exist(road1, road2))
