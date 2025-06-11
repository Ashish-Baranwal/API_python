import json

import requests
print("hello ashish123")

data = {
    "data" : "Dummy data for testing python script",
}

json_data = json.dumps(data) 

# URL for external POST request
url = 'https://431ba827-8835-466e-90db-ed648638ed90.mock.pstmn.io/InvokeBSL'
# url = 'https://httpbin.org/post'

# response = requests.post(url, json=json_data)
response = requests.post(url, data=json_data, headers={"Content-Type": "application/json"})

print(response.text)




# response = request.post(url, json=data)  # Use `json=data` to send JSON payload
# if response.status_code == 200:
#     print (jsonify({"message": "User created successfully", "response": response.json()}), 200)
# else:
#     print (jsonify({"error": "Failed to create user", "details": response.text}), response.status_code)



