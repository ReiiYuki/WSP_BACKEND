#Nature Drink BACKEND
##DATABASE INFORMATION   

  ```
  'ENGINE': 'django.db.backends.mysql',
  'NAME': 'naturedrink',
  'USER' : 'root',
  'HOST' : 'localhost',
  'PORT' : '3306'
  ```

  Please always import `naturedrink.sql` every time after pull.

##API information
  `api/v1/` - prefix API.

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

  `productoption` - product option system

  Method | URL | Header | Body | Description
  --- | --- | --- | --- | ---
  GET | container/option/ |  |  | Get list of product option
  POST | container/option/ | Authorization : Token `authenticate token` |
