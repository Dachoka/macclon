from django.test import TestCase
from .models import Image,Profile

# Create your tests here.
class ProfileTestCase(TestCase):
    '''
    Test case that runs test for the profile model objects
    '''

    def setUp(self):
       self.daisy = Profile(photo ='photos/dpic.jpeg', bio='Loving Life' )

    def test_instance(self):
        self.assertTrue(isinstance(self.daisy, Profile))


    def test_save_method(self):
        self.daisy.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)