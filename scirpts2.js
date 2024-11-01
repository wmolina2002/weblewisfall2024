function Execute() {
    var name = document.getElementById('name').value;
    var id = document.getElementById('id').value;
    console.log('Name:', name);
    console.log('ID:', id);
    // Create the JSON data
    var data = { name: name, id: id };

    // Send a POST request to the Flask route
    fetch('/request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function GetLast() {
    // Get the ID from the document
    var id = document.getElementById('id_search').value;
    // Fetch the last name from the Flask route
    fetch('/get_last_name?id=' + id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('last-name').innerText = data['last-name'];
    })
    .catch((error) => {
        console.error('Error:', error);
    });

}