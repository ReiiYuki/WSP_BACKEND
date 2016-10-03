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
  GET | member/detail/ | Authorization : Token `authenticate token` |  | Get list of member
  POST | member/detail/ |  | username , password , email , first_name , last_name | Create user
  GET | member/detail/`pk`/ | Authorization : Token `authenticate token` |  | Get user id `pk` info
  GET | member/detail/0/ | Authorization : Token `authenticate token` |  | Get current user
  POST | member/detail/change_password/ | Authorization : Token `authenticate token` | password , new_password | Change password
