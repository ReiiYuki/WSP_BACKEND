#Nature Drink BACKEND
##DATABASE INFORMATION   

  ```
  'ENGINE': 'django.db.backends.postgresql',
  'NAME': 'naturedrink',
  'USER' : 'postgres',
  'PASSWORD' : 'root1234',
  'HOST' : 'localhost',
  'PORT' : '5432'
  ```

  Please always import `naturedrink.sql` every time after pull.

##API information

  `api/v1/` - prefix API.
  `Authorization` - `Token auth-token`

User

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/u/login/ | No | { username,password } | Login user and get token  
POST | api/v1/u/user/ | No | { username,password,email,first_name,last_name } | Register new user  
GET | api/v1/u/user/ | Yes | No | Get list of user [Staff Only]
GET | api/v1/u/user/pk/ | Yes | No | Get user detail [Owner(Limit),Staff]
DELETE | api/v1/u/user/pk/ | Yes | No | Deactive user [Staff(Only Not Staff),Admin]
PUT | api/v1/u/user/change_password | Yes | { password,new_password } | Change password [Owner]
