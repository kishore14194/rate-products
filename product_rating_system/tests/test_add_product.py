from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token

from product.format_data import generate_pro_id


class UserRegisterTestCase(APITestCase):
    url_add = '/product/add/'

    def setUp(self):
        self.user1_username = "user1"
        self.user1_password = "123user!@#"
        self.user1_email = "user1@user.com"
        self.user1 = User.objects.create_user(username=self.user1_username, password=self.user1_password,
                                              email=self.user1_email, is_staff=True)
        self.auth_token1 = Token.objects.create(user=self.user1)
        self.user_token1 = self.auth_token1.key

        self.user2_username = "user2"
        self.user2_password = "123user!@#"
        self.user2_email = "user2@user.com"
        self.user2 = User.objects.create_user(username=self.user2_username, password=self.user2_password,
                                              email=self.user2_email)
        self.auth_token2 = Token.objects.create(user=self.user2)
        self.user_token2 = self.auth_token2.key

    def test_add_product_success(self):
        data = {
            "product_name": "foeeeee",
            "mrp": 122,
            "product_desc": "example second value"
        }

        response = self.client.post(self.url_add, data, format='json',
                                    HTTP_AUTHORIZATION='Token {token}'.format(token=self.auth_token1))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_forbid = self.client.post(self.url_add, data, format='json',
                                           HTTP_AUTHORIZATION='Token {token}'.format(token=self.auth_token2))
        self.assertEqual(response_forbid.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_product_failure(self):
        data_length_val = {
            "product_name": "fo",
            "mrp": 122,
            "product_desc": "example second value"
        }

        data_integer_val = {
            "product_name": "fo",
            "mrp": 122,
            "product_desc": "example second value"
        }

        data_missing = {}

        response_len = self.client.post(self.url_add, data_length_val, format='json',
                                        HTTP_AUTHORIZATION='Token {token}'.format(token=self.auth_token1))
        self.assertEqual(response_len.status_code, status.HTTP_400_BAD_REQUEST)

        response_int_val = self.client.post(self.url_add, data_integer_val, format='json',
                                            HTTP_AUTHORIZATION='Token {token}'.format(token=self.auth_token1))
        self.assertEqual(response_int_val.status_code, status.HTTP_400_BAD_REQUEST)

        response_missing = self.client.post(self.url_add, data_missing, format='json',
                                            HTTP_AUTHORIZATION='Token {token}'.format(token=self.auth_token1))
        self.assertEqual(response_missing.status_code, status.HTTP_400_BAD_REQUEST)


    def test_generate_pro_id(self):
        response_val = generate_pro_id('name')
        response_empty = generate_pro_id('')
        response_none = generate_pro_id(None)
