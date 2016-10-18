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
PUT | api/v1/u/user/change_password/ | Yes | { password,new_password } | Change password [Owner]
PUT | api/v1/u/user/pk/edit/ | Yes | { first_name,last_name,email } | Edit User [Owner(Limit),Staff[Only Not staff],Admin]

Address

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/u/address/ | Yes | {address_number,village,road,sub_distinct,distinct,province,country,zipcode} | Create Address
GET | api/v1/u/address/ | Yes | No | Get list of address [Owner(Limit),Staff]
GET | api/v1/u/address/pk/ | Yes | No | Get address [Owner(limit),Staff]
PUT | api/v1/u/address/pk/ | Yes | {address_number,village,road,sub_distinct,distinct,province,country,zipcode} |  Edit address [Owner(limit),Staff]
DELETE | api/v1/u/address/pk/ | Yes | No | Deactive address

Category

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/p/category/ | Yes | { name,description} | Add new Category [Staff]
GET | api/v1/p/category/ | No | No | List category [All(limit),Staff]
GET | api/v1/p/category/pk/ | No | No | Get category
PUT | api/v1/p/category/pk/ | Yes | { name,description } | Edit Category [Staff]
DELETE | api/v1/p/category/pk/ | Yes | No | Deactive Category [Staff]

Product

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/p/product/ | Yes | {name,description,price,category} | Add new Product [Staff]
