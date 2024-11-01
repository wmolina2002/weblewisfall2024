from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/get_last_name', methods=['GET'])
def get_last_name():
    # Get the ID from the GET request
    #id = request.headers.get('id')
    #adding random comments
    id = request.args.get('id')
    #id = request.headers.get('id')
    # Open the data.csv file and search for the matching ID
    with open("data.csv", "r") as f:
        for line in f:
            line_id, name = line.strip().split(',')
            if line_id == id:
                print(name)
                return jsonify({"last-name": name})

    # If no matching ID is found, return an error message
    return jsonify({"error": "ID not found"}), 404

@app.route('/request', methods=['POST'])
def get_json():
    # Parse the incoming JSON data
    json_data = request.get_json()

    id = json_data['id']
    name = json_data['name']

    #write code that takes in a user name and a user ID and write that to a CSV file called data.csv
    f = open("data.csv", "a")
    f.write(id + ','+ name + '\n')
    f.close()

    # Return the parsed JSON data as a response
    return jsonify(json_data)

@app.route('/')
def serve_main():
    return send_from_directory('.', 'main.html')

if __name__ == "__main__":
    app.run(debug=True)
