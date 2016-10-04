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
  GET | container/category/`pk` |  |  | Get category id `pk`
  GET | container/category/`pk`/product/ |  |  | Get list of product at category
  PUT | container/category/`pk`/ | Authorization : Token `authenticate token` | name , detail | Edit category [Admin]
