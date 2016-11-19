# Nature Drink BACKEND

## Front End

https://github.com/b5710546232/WSP_FRONTEND

## DATABASE INFORMATION   

```
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'naturedrink',
'USER' : 'postgres',
'PASSWORD' : 'root1234',
'HOST' : 'localhost',
'PORT' : '5432'
```

## User API

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
PUT | api/v1/t/order/pk/upload_slip/ | Yes | {transfer_slip} | Upload Slip
PUT | api/v1/t/order/pk/delete_slip/ | Yes | No | Delete Slip

Design

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/d/design/ | Yes | {'name','description','image'} | Add Design  
GET | api/v1/d/design/ | Yes | No | View Design list  
DELETE | api/v1/t/design/pk/ | Yes | No | Delete design
POST | api/v1/t/design/submit/ | Yes | | Submit Design Request
POST | api/v1/t/design/desubmit/ | Yes | | DeSubmit Design Request

Bottle

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/d/bottle/ | Yes | No | View Bottle for design list  

Logo

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/d/logo/ | Yes | No | View Logo for design list  

Bottle

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/d/bottle/ | Yes | No | View Bottle for design list  

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

Design

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/t/design/deconfirm/ | Yes | | deconfirm Design Request
POST | api/v1/t/design/confirm/ | Yes | | confirm Design Request

ฺBottle

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/m/bottle/ | Yes | {name,img,is_active} | Add new ฺBottle
GET | api/v1/m/bottle/ | No | No | List ฺBottle
GET | api/v1/m/bottle/pk/ | No | No | Get ฺBottle
PUT | api/v1/m/bottle/pk/ | Yes | {name,img,is_active} | Edit ฺBottle
DELETE | api/v1/m/bottle/pk/ | Yes | No | Deactive ฺBottle
PUT | api/v1/m/bottle/pk/reactive/ | Yes | No | Reactive ฺBottle

Logo

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/m/logo/ | Yes | {name,img,is_active} | Add new Logo
GET | api/v1/m/logo/ | No | No | List Logo
GET | api/v1/m/logo/pk/ | No | No | Get Logo
PUT | api/v1/m/logo/pk/ | Yes | {name,img,is_active} | Edit Logo
DELETE | api/v1/m/logo/pk/ | Yes | No | Deactive Logo
PUT | api/v1/m/logo/pk/reactive/ | Yes | No | Reactive Logo

Banner

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
POST | api/v1/m/banner/ | Yes | {name,img,is_active,bottle} | Add new Banner
GET | api/v1/m/banner/ | No | No | List Banner
GET | api/v1/m/banner/pk/ | No | No | Get Banner
PUT | api/v1/m/banner/pk/ | Yes | {name,img,is_active,bottle} | Edit Banner
DELETE | api/v1/m/banner/pk/ | Yes | No | Deactive Banner
PUT | api/v1/m/banner/pk/reactive/ | Yes | No | Reactive Banner

Stat   

Method | URL | Token | JSON | Description  
--- | --- | --- | --- | --- | ---
GET | api/v1/m/stat/product | No |  | Stat of Amount Product
GET | api/v1/m/stat/category | No |  | Stat of Amount category
GET | api/v1/m/stat/money | No |  | Stat of Money Product
GET | api/v1/m/stat/user/payment | No |  | Stat of Amount payment Product of user
GET | api/v1/m/stat/user/order | No |  | Stat of Amount Order of user
GET | api/v1/m/stat/user/shipping | No |  | Stat of Amount shipped order of user
GET | api/v1/m/stat/address | No |  | Stat of Amount Address
