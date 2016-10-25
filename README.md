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
GET | api/v1/u/user/is_admin/ | Yes | No | True if admin [Admin Only]
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
GET | api/v1/p/category/pk/product/ | No | No | Get product in category
PUT | api/v1/p/category/pk/ | Yes | { name,description } | Edit Category [Staff]
DELETE | api/v1/p/category/pk/ | Yes | No | Deactive Category [Staff]
PUT | api/v1/p/category/pk/reactive/ | Yes | No | Reactive Category [Staff]

Product

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/p/product/ | Yes | {name,description,price,category} | Add new Product [Staff]
GET | api/v1/p/product/ | No | No | List product [All(limit),Staff]
GET | api/v1/p/product/pk/ | No | No | Get product
PUT | api/v1/p/product/pk/ | Yes | {name,description,price,category} | Edit Product  [Staff]
DELETE | api/v1/p/product/pk/ | Yes | No | Deactive Product [Staff]
PUT | api/v1/p/product/pk/reactive/ | Yes | No | Reactive Product [Staff]

Product Option (Inactive)

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/p/option/ | Yes | {name,product} | Add new Product Option [Staff]
GET | api/v1/p/option/ | No | No | List product option [All(limit),Staff]
GET | api/v1/p/option/pk/ | No | No | Get product option
PUT | api/v1/p/option/pk/ | Yes | {name,product} | Edit Product Option  [Staff]
DELETE | api/v1/p/option/pk/ | Yes | No | Deactive Product Option [Staff]
PUT | api/v1/p/option/pk/reactive/ | Yes | No | Reactive Product Option [Staff]

Product Choice (Inactive)

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/p/choice/ | Yes | {name,option} | Add new Product choice [Staff]
GET | api/v1/p/choice/ | No | No | List product choice [All(limit),Staff]
GET | api/v1/p/choice/pk/ | No | No | Get product choice
PUT | api/v1/p/choice/pk/ | Yes | {name,option} | Edit Product choice  [Staff]
DELETE | api/v1/p/choice/pk/ | Yes | No | Deactive Product choice [Staff]
PUT | api/v1/p/choice/pk/reactive/ | Yes | No | Reactive Product choice [Staff]

Payment Method

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/t/method/ | Yes | {name,type} | Add new Payment Method [Staff]
GET | api/v1/t/method/ | No | No | List Payment Method [All(limit),Staff]
GET | api/v1/t/method/pk/ | No | No | Get Payment Method
PUT | api/v1/t/method/pk/ | Yes | {name,type} | Edit Payment Method  [Staff]
DELETE | api/v1/t/method/pk/ | Yes | No | Deactive Payment Method [Staff]
PUT | api/v1/t/method/pk/reactive/ | Yes | No | Reactive Payment Method [Staff]

Cart

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/t/cart/ | Yes | {product,quantity} | Add Item to cart  
GET | api/v1/t/cart/ | Yes | No | View Cart list  
PUT | api/v1/t/cart/pk/ | Yes | {product,quantity} | Edit Item in cart
DELETE | api/v1/t/cart/pk/ | Yes | No | Delete item form cart
POST | api/v1/t/cart/pay/ | Yes | {address,method} | Pay item in cart

Property (Inactive)

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/t/property/ | Yes | {option,choice} | Add option for line item  
GET | api/v1/t/property/pk/ | Yes | No | Get property

Order

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/t/order/ | Yes | No | Get list of order
GET | api/v1/t/order/pk | Yes | No | Get order
PUT | api/v1/t/order/pk/update_track/ | Yes | {postal_track} | Update Postal Track
DELETE | api/v1/t/order/pk/delete_track/ | Yes | No | Delete Postal Track
PUT | api/v1/t/order/pk/confirm | Yes | No | Confirm Payment
DELETE | api/v1/t/order/pk/deconfirm | Yes | No | Unconfirm Payment
