import requests

print("Welcome to the is-it-down-detector")
url = input("Enter the website you'd like to check: ")
res = requests.get(url)
print("That website is", "up!" if res.status_code == 200 else "down!")
