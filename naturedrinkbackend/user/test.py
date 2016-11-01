from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserTest(APITestCase) :

    def test_register_user(self):
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_incomplete_register_user(self):
        data = {"password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        data = {"username":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        data={"username":"test","password":"test"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        token = Token.objects.get(user__username='test')
        self.assertEqual(response.data['token'],token.key)

    def test_login_fail_user(self):
        data={"username":"test","password":""}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_get_user_anonymous(self):
        response = self.client.get('/api/v1/u/user/0/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_get_user(self) :
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        data={"username":"test","password":"test"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/v1/u/user/0/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,{'id':response.data['id'],'username':'test','is_active':True,'first_name':'test','last_name':'test','email':'test@test.test'})

    def test_change_password(self):
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        data={"username":"test","password":"test"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        data = {"password":"test","new_password":"A"}
        response = self.client.put('/api/v1/u/user/change_password/',data,type="json")
        data={"username":"test","password":"test"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
        data={"username":"test","password":"A"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_edit_user(self) :
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        data={"username":"test","password":"test"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/v1/u/user/0/')
        id = response.data['id']
        data = {"first_name":"A","last_name":"B","email":"A@B.C"}
        response = self.client.put(('/api/v1/u/user/'+str(id)+'/edit/'),data,format="json")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/v1/u/user/0/')
        self.assertEqual(response.data['first_name'],"A")
        self.assertEqual(response.data['last_name'],"B")
        self.assertEqual(response.data['email'],"A@B.C")

    def test_is_admin_user(self) :
        user = User.objects.create(username="a",password="b",is_staff=True,is_superuser=True)
        token = Token.objects.get(user__username='a')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get('/api/v1/u/user/is_admin/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_is_not_admin(self):
        data = {"username":"test","password":"test","first_name":"test","last_name":"test","email":"test@test.test"}
        response = self.client.post('/api/v1/u/user/',data,format="json")
        data={"username":"test","password":"test"}
        response = self.client.post('/api/v1/u/login/',data,format="json")
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        response = self.client.get('/api/v1/u/user/is_admin/')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
