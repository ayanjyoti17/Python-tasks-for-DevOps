# Program to demonstrate integration with GitHub to fetch the 
# details of Users who created Pull requests(Active) on Kubernetes Github repo.
import requests

# URL to fetch pull requests from the GitHub API
url = f'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Make a GET request to fetch pull requests data from the GitHub API
response = requests.get(url)  

complete_detail =response.json()
for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])