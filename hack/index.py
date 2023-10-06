import requests

def brute_force(target_password, character_set, username, password):
    for length in range(1, len(target_password) + 1):
        for candidate in generate_combinations(character_set, length):
            print(candidate)  # Добавлен этот вывод

            # Отправляем запрос на сайт
            url = "http://ваш_сайт.com/login"  # Замените на ваш реальный URL
            payload = {"username": username, "password": password}
            cookies = {"username": username, "password": password}  # Устанавливаем куки
            response = requests.post(url, data=payload, cookies=cookies)

            if response.status_code == 200:
                print(f"Ответ от сервера: {response.text}")

            if candidate == target_password:
                return candidate

def generate_combinations(character_set, length):
    if length == 1:
        return character_set
    else:
        return [char + combination for char in character_set for combination in generate_combinations(character_set, length - 1)]

# Ваш остальной код остается неизменным

target_password = "123"
character_set = "0123456789"
username = "ваш_логин"  # Замените на ваш реальный логин
password = "ваш_пароль"  # Замените на ваш реальный пароль

found_password = brute_force(target_password, character_set, username, password)

if found_password:
    print(f"Пароль найден: {found_password}")
else:
    print("Пароль не найден.")
