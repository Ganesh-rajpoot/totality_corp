from rest_framework.test import APITestCase
from .views import *
from django.urls import reverse
from rest_framework import status

class UserDetailsGetTest(APITestCase):
    def setUp(self):
        self.url = reverse("userdetails")

    def test_get_all_user_details(self):
        response = self.client.get(reverse('userdetails'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_user_details(self):
        data = {
            "fname": "John",
            "city": "New York",
            "phone": 1234567890,
            "height": 5.8,
            "married": True
        }
        response = self.client.post(reverse('userdetails'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



class UserDetailsViewTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            "id": 1,
            "fname": "Stave",
            "city": "LA",
            "phone": 1234567890,
            "height": 5.8,
            "married": True
        }
        self.user = UserDetails.objects.create(**self.user_data)
        

    def test_get_user_details(self):
        self.user.id = 1
        url = reverse('userdetail', kwargs={'pk': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_details(self):
        url = reverse('userdetail', kwargs={'pk': self.user.id})  
        updated_data = {
            "fname": "updated_user",
            "city": "Test",
            "phone": 1234467890,
            "height": 5.8,
            "married": False
            
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_partial_update_user_details(self):
        url = reverse('userdetail', kwargs={'pk': self.user.id})  
        partial_data = {
            "fname": "partialy_test fname",
            
        }
        response = self.client.patch(url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_user_details(self):
        url = reverse('userdetail', kwargs={'pk': self.user.id})  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

