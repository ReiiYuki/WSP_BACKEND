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

##User API

  `api/v1/` - prefix API.
  `Authorization` - `Token auth-token`

User

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/u/login/ | No | { username,password } | Login user and get token  
POST | api/v1/u/user/ | No | { username,password,email,first_name,last_name } | Register new user  
GET | api/v1/u/user/is_admin/ | Yes | No | True if admin [Admin Only]
GET | api/v1/u/user/0/ | Yes | No | Get user detail Owner
PUT | api/v1/u/user/change_password/ | Yes | { password,new_password } | Change password
PUT | api/v1/u/user/pk/edit/ | Yes | { first_name,last_name,email } | Edit User

Address

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/u/address/ | Yes | {address_number,village,road,sub_distinct,distinct,province,country,zipcode} | Create Address
GET | api/v1/u/address/pk/ | Yes | No | Get address
PUT | api/v1/u/address/pk/ | Yes | {address_number,village,road,sub_distinct,distinct,province,country,zipcode} |  Edit address
DELETE | api/v1/u/address/pk/ | Yes | No | Deactive address

Category

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/p/category/ | No | No | List category
GET | api/v1/p/category/pk/ | No | No | Get category
GET | api/v1/p/category/pk/product/ | No | No | Get product in category

Product

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/p/product/ | No | No | List product
GET | api/v1/p/product/pk/ | No | No | Get product

Payment Method

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/t/method/pk/ | No | No | Get Payment Method

Cart

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/t/cart/ | Yes | {product,quantity} | Add Item to cart  
GET | api/v1/t/cart/ | Yes | No | View Cart list  
GET | api/v1/t/cart/lines/ | Yes | No | View all of item line
PUT | api/v1/t/cart/pk/ | Yes | {product,quantity} | Edit Item in cart
DELETE | api/v1/t/cart/pk/ | Yes | No | Delete item form cart
POST | api/v1/t/cart/pay/ | Yes | {address,method} | Pay item in cart

Order

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/t/order/ | Yes | No | Get list of order
GET | api/v1/t/order/pk | Yes | No | Get order
PUT | api/v1/t/order/pk/update_track/ | Yes | {postal_track} | Update Postal Track
DELETE | api/v1/t/order/pk/delete_track/ | Yes | No | Delete Postal Track
PUT | api/v1/t/order/pk/confirm | Yes | No | Confirm Payment
DELETE | api/v1/t/order/pk/deconfirm | Yes | No | Unconfirm Payment
PUT | api/v1/t/order/pk/upload_slip/ | Yes | {transfer_slip} | Upload Slip
PUT | api/v1/t/order/pk/delete_slip/ | Yes | No | Delete Slip

## Administrator API  

  User

  Method | URL | Token | JSON | Description  
  --- | --- | --- | --- | --- | ---
  GET | api/v1/m/user/ | Yes | No | Get list of user
  GET | api/v1/m/user/pk/ | Yes | No | Get user info
  POST | api/v1/m/user/ | Yes | {username,password,first_name,last_name,email,is_active,is_staff} | Create new user
  PUT | api/v1/m/user/pk/ | Yes | {first_name,last_name,is_active,is_staff,email} | Update user
  DELETE | api/v1/m/user/pk/ | Yes | No | Deactive User
  PUT | api/v1/m/user/pk/reactive/ | Yes | No | Reactive User
  PUT | api/v1/m/user/pk/assign_staff/ | Yes |No | Assign Staff
  PUT | api/v1/m/user/pk/fire_staff/ | Yes | No Fire Staff

  Address

  Method | URL | Token | JSON | Description  
  --- | --- | --- | --- | --- | ---
  GET | api/v1/m/address/ | Yes | No | Get List of address
  GET | api/v1/m/address/pk/ | Yes | No | Get address info
  POST | api/v1/m/address/ | Yes | {address_number,village,road,sub_distinct,distinct,province,country,zipcode,is_active,user} | Create Address
  PUT | api/v1/m/address/pk/ | Yes | {address_number,village,road,sub_distinct,distinct,province,country,zipcode,is_active,user} | Update Address

  Product

  Method | URL | Token | JSON | Description  
  --- | --- | --- | --- | --- | ---
  GET | api/v1/m/product/ | Yes | No | Get List of product
  GET | api/v1/m/product/pk/ | Yes | No | Get product info
  POST | api/v1/m/product/ | Yes | {image,name,description,price,category,is_active} | Create product
  PUT | api/v1/m/product/pk/ | Yes | {name,image,description,price,category,is_active} | Update product
  DELETE | api/v1/m/product/pk/ | Yes | No | Deactive product
  PUT | api/v1/m/product/pk/reactive/ | Yes | No | Reactive product

  Category

  Method | URL | Token | JSON | Description  
  --- | --- | --- | --- | --- | ---
  GET | api/v1/m/category/ | Yes | No | Get List of category
  GET | api/v1/m/category/pk/ | Yes | No | Get category info
  POST | api/v1/m/category/ | Yes | {name,description,is_active} | Create category
  PUT | api/v1/m/category/pk/ | Yes | {name,description,is_active} | Update category
  DELETE | api/v1/m/category/pk/ | Yes | No | Deactive Category
  PUT | api/v1/m/category/pk/reactive/ | Yes | No | Reactive Category

  Payment Method

  Method | URL | Token | JSON | Description  
  --- | --- | --- | --- | --- | ---
  POST | api/v1/m/method/ | Yes | {name,type,is_active} | Add new Payment Method
  GET | api/v1/m/method/ | No | No | List Payment Method
  GET | api/v1/m/method/pk/ | No | No | Get Payment Method
  PUT | api/v1/m/method/pk/ | Yes | {name,type,is_active} | Edit Payment Method
  DELETE | api/v1/m/method/pk/ | Yes | No | Deactive Payment Method
  PUT | api/v1/m/method/pk/reactive/ | Yes | No | Reactive Payment Method

  Item Line

  Method | URL | Token | JSON | Description  
  --- | --- | --- | --- | --- | ---
  GET | api/v1/m/item_line/ | Yes | No | View itemline list  

  Order

  Method | URL | Token | JSON | Description  
  --- | --- | --- | --- | --- | ---
  GET | api/v1/m/order/ | Yes | No | View order list  
  PUT | api/v1/m/order/pk/confirmPayment/ | Yes | No | Confirm paymentation of order
  PUT | api/v1/m/order/pk/updateTrack/ | Yes | {track} | update postal track of order
  PUT | api/v1/m/order/pk/deleteTrack/ | Yes | No | delete postal track of order
  PUT | api/v1/m/order/pk/unconfirmPayment/ | Yes | No | Unconfirm paymentation of order
