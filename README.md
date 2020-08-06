
# drf- backend-service

A photos backend service made in django rest framework


# Host

App is deployed at https://dev-api-photos.herokuapp.com


#	API doc
- /auth/jwt/register/ 

  `Supported methods - POST`
   
   `Expected payload format  { "username":"user", "password":"123",  "password2":"123", "email":"user@sample.com" }`

- /auth/jwt/token/
- /auth/jwt/refresh/

- /photos/  
`Supported methods - GET/POST/PUT/PATCH/DELETE`

