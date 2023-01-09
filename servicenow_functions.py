#Need to install requests package for python
#easy_install requests
import requests

#ServiceNow REST API Request Function
def snam_request(request, user, pwd, instance, table, query):
    #Set the request parameters
    if query != '':
        url = 'https://' + instance + '.service-now.com/api/now/table/' + table + '/' + query
    else:
        url = 'https://' + instance + '.service-now.com/api/now/table/' + table
    #Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    #Do the HTTP request
    if request == 'get':
        response = requests.get(url, auth=(user, pwd), headers=headers)
    elif request == 'patch':
        response = requests.patch(url, auth=(user, pwd), headers=headers)
    elif request == 'put':
        response = requests.put(url, auth=(user, pwd), headers=headers)
    elif request == 'post':
        response = requests.post(url, auth=(user, pwd), headers=headers)
    elif request == 'delete':
        response = requests.delete(url, auth=(user, pwd), headers=headers)
    #Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()
    #Decode the JSON response into a dictionary and return the data
    return response.json()['result']