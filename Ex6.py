import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print(f"Количество редиректов - {len(response.history)}")
print(f"URL итоговый - {response.url}")

