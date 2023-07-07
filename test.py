from route_exist import Point, Road, route_exist


def test_route_exist():
    # Создаем точки
    point_a = Point(55.7522, 37.6156)
    point_b = Point(59.9343, 30.3351)
    point_c = Point(52.5200, 13.4050)

    # Создаем дороги
    road_1 = Road(point_a, point_b)
    road_2 = Road(point_b, point_c)
    road_3 = Road(point_c, point_a)

    # Проверяем наличие маршрута
    assert route_exist(road_1, road_2) == True
    assert route_exist(road_2, road_3) == True
    assert route_exist(road_3, road_1) == True

    # Создаем новую точку и дорогу без связи
    point_d = Point(40.7128, -74.0060)
    road_4 = Road(point_a, point_d)

    # Проверяем отсутствие маршрута
    assert route_exist(road_1, road_4) == False

    print("Все тесты пройдены успешно!")


# Запускаем тесты
test_route_exist()