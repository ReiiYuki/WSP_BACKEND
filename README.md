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

  `member` - member system.
  | Method |      URL    |                   Header                   |                         Body                         |      Description      |
  | ------ |:-----------:|:------------------------------------------:|:----------------------------------------------------:|:---------------------:|
  | POST   | login/      |                                            | username , password                                  | Login user            |
  | GET    | member/     | Authorization : Token `authenticate token` |                                                      | Get list of member    |
  | POST   | member/     |                                            | username , password , email , first_name , last_name | Create user           |
  | GET    | member/`pk` | Authorization : Token `authenticate token` |                                                      | Get user id `pk` info |
  | GET    | member/0    | Authorization : Token `authenticate token` |                                                      | Get current user      |
