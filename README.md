# drf- backend-service

A photos backend service made in django rest framework


# Host

App is deployed at https://dev-api-photos.herokuapp.com


#	API doc
- /auth/jwt/register 
Method: POST
Register new user to get JWT access token
Use payload eg 
{ "username":"user", "password":"123", "password2":"123", "email":"user@sample.com"}
Copy access token received and use it in Authorization header : Bearer <access token>

- /auth/jwt/token
- /auth/jwt/refresh

- /photos/  
Please follow RESTful principles to access GET/POST/DELETE/PUT/PATCH for resources
