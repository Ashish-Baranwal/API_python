from flask import Flask, request, jsonify
import requests, json

app = Flask(__name__)

# URL for external POST request
url = 'https://431ba827-8835-466e-90db-ed648638ed90.mock.pstmn.io/InvokeBSL'
received_data = {}

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@gmail.com"
    }

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    received_data = request.get_json()

    
    if not received_data:
        return jsonify({"error": "Invalid input"}), 400
    
    transformed_data = transform_data(received_data)

    print("received data type", type(received_data))
    print("transformed data type", type(transformed_data))
    print("Transformed Data: ", transformed_data)
    
    response = requests.post(url, json= transformed_data)  # Use `json=received_data` to send JSON payload
    print(response.text)  # Print the response from the external server

    if response.status_code == 200:
        return jsonify({"message": "User created successfully", "response": response.json()}), 200
    else:
        return jsonify({"error": "Failed to create user", "details": response.text}), response.status_code

def transform_data(input_data):

    transformed_data = {}

    transformed_data['FirstName'] = input_data.get('FirstName') or "Not Specified"
    transformed_data['LastName'] = input_data.get('LastName') or "Not Specified"
    transformed_data['ZipCode'] = input_data.get('ZipCode') or "Not Specified"
    transformed_data['phoneNumber'] = input_data.get('phoneNumber') or None
    transformed_data['Email'] = input_data.get('Email') or None
    transformed_data['JobId'] = input_data.get('JobId') or None
    transformed_data['Source'] = input_data.get('Source') or None
    transformed_data['IsEasyApplyWithTalent'] = input_data.get('IsEasyApplyWithTalent') or None
    transformed_data['Documents'] = input_data.get('Documents') or None

    return transformed_data


if __name__ == "__main__":
    app.run(debug=True)