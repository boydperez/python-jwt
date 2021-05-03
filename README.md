## JSON Web Token (JWT) 

JWT demonstration using python flask micro web framework with basic http access authentication for token access.

### Installation

1. Create a virtual environment and install all the dependencies according to your OS
2. Start the server
3. Go to `http://localhost:5000`

### Usage  

This demo consists of 3 endpoints.

#### /public endpoint

Accessible to the public without any authentication.

#### /authenticate endpoint

Default username and password for http Authentication.
Username: username
Password: password

**or set the credentials using environment variables.**

Returns a json response with a payload of {'message': [token]}

#### /private endpoint

Use the above token and pass it as a query string.

`http://localhost:5000/private?token=[token]`

And there you go, you have access to the private endpoint.
