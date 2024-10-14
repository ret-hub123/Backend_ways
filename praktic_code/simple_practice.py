import os

def curl_method_prog():
    request = input("Введите команду: ")
    if request.upper() in ["GET", "POST", "PUT", "DELETE"]:
        os.system(f"curl -X {request.upper()} -i -v https://www.google.ru")
    else:
        print("Неверно введёт запрос.")

curl_method_prog()