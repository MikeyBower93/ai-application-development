import requests

response = requests.get('http://www.testingmcafeesites.com/testcat_be.html')


print(response.status_code)