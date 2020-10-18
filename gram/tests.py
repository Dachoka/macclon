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

    def test_update_method(self):
        self.daisy.save_profile()
        self.daisy = Profile.objects.filter(bio = 'Loving Life').update(bio = 'Awesomeness')
        self.profile_update = Profile.objects.get(photo='photos/dpic.jpeg')
        self.assertEqual(self.profile_update.bio, 'Awesomeness')

    def test_delete_method(self):
        self.daisy.save_profile()
        self.daisy = Profile.objects.get(photo = 'photos/dpic.jpeg')
        self.daisy.delete_profile()
        profiles= Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ImageTestCase(TestCase):
    '''
    Testcase that runs tests for image model objects
    '''
    def setUp(self):
        self.machoka = Profile(photo = 'photos/propic.jpg', bio = 'Live love laugh')
        self.machoka.save_profile()
        self.photoshoot = Image(image = 'photos/shoot.jpeg',name = 'My Photoshoot', caption = 'Pose', profile = self.machoka,likes=1, comments='Nice')

    def test_instance(self):
        self.assertTrue(isinstance(self.photoshoot, Image))

    def test_save_method(self):
        self.photoshoot.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_update_method(self):
        self.photoshoot.save_image()
        self.photoshoot = Image.objects.filter(caption = 'Pose').update(caption = 'pretty pink')
        self.image_update = Image.objects.get(image = 'photos/shoot.jpeg')
        self.assertEqual(self.image_update.caption,'pretty pink' )

    def test_delete_method(self):
        self.photoshoot.save_image()
        self.photoshoot = Image.objects.get(image = 'photos/shoot.jpeg')
        self.photoshoot.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
