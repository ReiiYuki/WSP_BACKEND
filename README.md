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

###Member System
  `member` - member system.   

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  POST | login/ |  | username , password | Login user and Get Token
  GET | member/detail/ | Authorization : Token `authenticate token` |  | Get list of member [OwnerOrAdmin]
  POST | member/detail/ |  | username , password , email , first_name , last_name | Create user
  GET | member/detail/`pk`/ | Authorization : Token `authenticate token` |  | Get user id `pk` info [OwnerOrAdmin]
  GET | member/detail/0/ | Authorization : Token `authenticate token` |  | Get current user [OwnerOrAdmin]
  PUT | member/detail/change_password/ | Authorization : Token `authenticate token` | password , new_password | Change password [OwnerOrAdmin]
  PUT | member/detail/edit_info/ | Authorization : Token `authenticate token` | first_name , email , last_name | Edit user info [OwnerOrAdmin]

  `address` - address system.

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  GET | member/address/`pk` | Authorization : Token `authenticate token` |  | Get address id `pk` info [OwnerOrAdmin]
  POST | address/ | Authorization : Token `authenticate token` | address , village , road , sub_district , district , province , country , zipcode | Create address [OwnerOrAdmin]
  PUT | address/ | Authorization : Token `authenticate token` | address , village , road , sub_district , district , province , country , zipcode | Update address [OwnerOrAdmin]
  DELETE | address/`pk` | Authorization : Token `authenticate token` |  | Delete Address id `pk` [OwnerOrAdmin]
  GET | address/ | Authorization : Token `authenticate token` |  | Get list of address [OwnerOrAdmin]

###Product System

  `category` - category system.     

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  GET | container/category/ |  |   |  Get list of category
  POST | container/category/ | Authorization : Token `authenticate token` | name , detail | Create category [Admin]
  GET | container/category/`pk`/ |  |  | Get category id `pk` with product
  PUT | container/category/`pk`/ | Authorization : Token `authenticate token` | name , detail | Edit category [Admin]
  DELETE | container/category/`pk`/ | Authorization : Token `authenticate token` |  | Delete category [Admin]

  `product` - product system

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  GET | container/product/ |  |  | Get list of product
  POST | container/product/ | Authorization : Token `authenticate token` | name , detail , price , category , options[ { name , choices[ { name } ] } ] | Create product with options and choices [Admin]
  GET | container/product/`pk`/ |  |  | Get product with options and choices
  PUT | container/product/`pk`/ | Authorization : Token `authenticate token` | name , detail , price , category | Edit product detail [Admin]

####Product Property

  `productoption` - product option system

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  GET | container/option/ |  |  | Get list of product option
  POST | container/option/ | Authorization : Token `authenticate token` | name , product | Create new product option
  GET | container/option/`pk`/ |  |  | Get product option
  PUT | container/option/`pk`/ | Authorization : Token `authenticate token` | name , product | Edit product option

  `productchoice` - product choice system

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  GET | container/choice/ |  |  | Get list of product choice
  POST | container/choice/ | Authorization : Token `authenticate token` | name , option | Create new product choice
  GET | container/choice/`pk`/ |  |  | Get product choice
  PUT | container/choice/`pk`/ | Authorization : Token `authenticate token` | name , option | Edit product choice

###Cart Service

  `cart` - cart service system

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  GET | action/cart/ | Authorization : Token `authenticate token` |  | View item in cart
  POST | action/cart/ | Authorization : Token `authenticate token` | product , quantity , option[ id , choice ] | Add product to cart
  GET | action/cart/`pk`/ | Authorization : Token `authenticate token` |  | Get product in cart
  DELETE | action/cart/`pk`/ | Authorization : Token `authenticate token` |  | Delete product from cart   
  POST | action/cart/pay/ | Authorization : Token `authenticate token` |  | Pay all product in cart
  PUT | action/cart/`pk`/ | Authorization : Token `authenticate token` | product , quantity , option[ id , choice ] | Edit product in cart  
