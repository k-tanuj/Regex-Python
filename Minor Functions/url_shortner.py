import requests

data = input("enter the url: ")

api_url = "https://tinyurl.com/api-create.php?url=" + data

response = requests.get(api_url).text

print("shortened url is: ", response)