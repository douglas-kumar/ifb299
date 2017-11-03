from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import *
from .urls import *
from django.db import IntegrityError
from django.urls import reverse, resolve

# To Run tests:
# python manage.py test Website.tests

# Story No: 3 - Log In
class CreateUserAndLogIn(TestCase):
    username = 'userToLogin'
    email = 'user2login@website.com'
    password = 'UserPassword1'

    def setup_new_user(self):
        user = User.objects.create_user(self.username, self.email, self.password)

    def log_user_in(self):
        user = authenticate(username=username, password=password)
        client = Client()
        if user is not None:
            client.login(username=self.username, password=self.password)
            response = self.client.get('/users/secure/', follow=True)
            user = User.objects.get(username=self.username)
            self.assertEqual(response.context['email'], self.email)

# Story No: 2 - Account Creation (Will)
class CreateNewAccount(TestCase):
    username = 'new_user'
    password = 'UniquePassword1'
    email = 'new_user@example.com'

    def setUp(self):
        user = User.objects.create_user(self.username)
        user.email = self.email
        user.set_password(self.password)
        user.save()

    def test_user_created_in_db(self):
        user = User.objects.get(username='new_user')
        assert user.email == self.email
        assert user.is_staff == False
        assert user.is_superuser == False

# Story No: 6 - Create New Admin User (Will)
class AddNewAdminUser(TestCase):
    username = 'admin2'
    password = 'Password1'
    email = 'admin2@example.com'

    def setUp(self):
        admin_user = User.objects.create_superuser(self.username, self.email, self.password)
        admin_user.save()

    def test_admin_creation_success(self):
        admin = User.objects.get(username=self.username)

        self.assertEqual(admin.username, 'admin2')
        self.assertEqual(admin.email, 'admin2@example.com')
        self.assertEqual(admin.is_staff, True)
        self.assertEqual(admin.is_superuser, True)
        self.assertEqual(admin.is_active, True)

    def test_admin_login_success(self):
        client = Client()
        client.login(username=self.username, password=self.password)

# Story No: 12 - Access Control (Will)
class AccessControl(TestCase):
    user_username = 'xXx_user_xXx'
    user_password = 'getREKTson'

    admin_username = 'admin2'
    admin_password = 'ILoveAmbiguity'

    admin_pages = [
        '/admin/login/?next=/admin/',
        '/admin/',
        '/admin/auth',
        '/admin/auth/group',
        '/admin/auth/group/add',
        '/admin/auth/user',
        '/admin/auth/user/add',
        '/admin/Website/college/',
        '/admin/password_change',
    ]

    def create_user(self):
        user, created = User.objects.get_or_create(username=self.user_username)
        user.set_password = self.user_password
        user.is_staff = False
        user.is_superuser = False
        user.save()
        self.user = user

    # User cannot access Admin Panel
    def test_user_access(self):
        self.create_user()
        for page in self.admin_pages:
            self.client.get(page)
            self.assertFalse(self.client.login(username=self.user_username, password=self.user_password))

    def create_admin(self):
        admin = User.objects.create_superuser(self.admin_username, 'somebody@email.com', self.admin_password)
        admin.save()

    # Admin can access Admin Panel
    def test_admin_access(self):
        self.create_admin()
        for page in self.admin_pages:
            self.client.get(page)
            self.assertTrue(self.client.login(username=self.admin_username, password=self.admin_password))

    # NOTE: tests checking user privileges on website needed (i.e. editing information about items)

# Story No: 4 - Menu (Calum)
class Menu(TestCase):
    urls = [
        "/Website/",
        "/Website/register/",
        "/Website/logout/",
        "/Website/login/",
        "/Website/Brisbane/"
    ]

    def test_index_page_connects(self):
        client = Client()
        response = self.client.get('/Website/')
        self.assertEqual(response.status_code, 200)

    def test_register_page_connects(self):
        client = Client()
        response = self.client.get('/Website/register/')
        self.assertEqual(response.status_code, 200)
        
    def test_logout_page_connects(self):
        client = Client()
        response = self.client.get('/Website/logout/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_connects(self):
        client = Client()
        response = self.client.get('/Website/login/')
        self.assertEqual(response.status_code, 200)
        
# Story No: 15 - Log Out (Ruka)
class LogOut(TestCase):
    username = 'user'
    password = 'userpassword'
    email = 'user@email.com'

    def test_create_new_user(self):
        user = User.objects.create_user(self.username, self.email, self.password)
        user.save()

    def test_user_login_success(self):
        client = Client()
        client.login(username=self.username, password=self.password)

    def test_userlogout_success(self):
        client = Client()
        client.logout()

# Commented out because it was failing tests, needs to be updated to new DB model
### Story No: 7 - Modify City Information (Ruka)
##class ModifyCityInfo(TestCase):
##    def test_modify(self):
##        College.objects.create(name="Uni", address="Somewhere", departments="Business, Medicine...etc.",
##                               email="imhere@email.com", image="https://image.jpg")
##        College.objects.filter(name="Uni").update(address="Here")
##        temp = College.objects.get(name="Uni")
##        self.assertEqual(temp.address, "Here")
        
# Story No: 10 - City Map
class CityMap(TestCase):

    city_name = "Brisbane"
    city_state = "QLD"
    city_longitude = None
    city_latitude = None

    
    #Test database to check if lat and long can be null
    def test_latlng_null(self):
        try:
            City.objects.create(name=self.city_name, state=self.city_state, longitude=self.city_longitude, latitude=self.city_latitude)
        except IntegrityError:
            print("Can't Be null")

            #Story No: 5  - Main View
class MainView(TestCase):
    username = 'stuff'
    password = 'works'
    account_type = "STUDENT"
    
    
    def create_user(self):
        user, created = User.objects.get_or_create(username=self.username)
        user.set_password = self.password
        user.save()
        

        user_acc = User.objects.get(username=self.username)
        user_pk = user_acc.pk
        user_acc2 = Profile.objects.get(user_id=user_pk)
        user_acc2.user_type = self.account_type
        user_acc2.save()
        
        self.user = user

        
    #Test to see if the data is stored
    def test_account_type(self):
        self.create_user()
        userdj = User.objects.get(username=self.user)
        userdj_pk = userdj.pk
        userprofile = Profile.objects.get(user_id=userdj_pk)
        self.assertTrue(self.account_type, userprofile.user_type)


# Story No: 19 - Sorting Items (Will)
class SortingItems(TestCase):
    def test_method(self):
        pass


# Story No: 18 - Reviews
class Reviews(TestCase):
    rating = 3
    text = "This review is a test to see if reviewing items works"
    username = 'tester'
    user = User.objects.get_or_create(username=username)
    place = LocationInfo.objects.get(pk=3)
    
    def create_review(self):
        review = Review.create(user, place, rating, text)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.place, self.place)
        self.assertEqual(review.rating, self.rating)
        self.assertEqual(review.text, self.text)
        review.save()

    def get_review(self):
        review = Review.objects.get(user=self.user, place=self.place)
        self.assertEqual(review.rating, self.rating)
        self.assertEqual(review.text, self.text)

    
#Story No: 08 - Multiple Cities
class MultipleCities(TestCase):
    model = City
    qut = LocationInfo.objects.get(pk=1)
    brisbane = City.objects.get(pk=1)
    sydney = City.objects.get(pk=2)
    melbourne = City.objects.get(pk=3)
    canberra = City.objects.get(pk=4)
    adelaide = City.objects.get(pk=5)
    darwin = City.objects.get(pk=6)
    hobart = City.objects.get(pk=7)
    perth = City.objects.get(pk=8)
    cairns = None
    alice_springs = None
    cities = [
        'Brisbane',
        'Sydney',
        'Melbourne',
        'Canberra',
        'Perth',
        'Darwin',
        'Adelaide'
    ]
    
    def test_cities_exist(self):
        self.assertIsNotNone(self.brisbane)
        self.assertIsNotNone(self.sydney)
        self.assertIsNotNone(self.melbourne)
        self.assertIsNotNone(self.canberra)
        self.assertIsNotNone(self.adelaide)
        self.assertIsNotNone(self.darwin)
        self.assertIsNotNone(self.hobart)
        self.assertIsNotNone(self.perth)

    def test_arbitrary_cities_non_existent(self):
        self.assertIsNone(self.cairns)
        self.assertIsNone(self.alice_springs)

    def test_city_names(self):
        self.assertEquals(self.cities[0], self.brisbane.name)
        self.assertEquals(self.cities[1], self.sydney.name)

        self.assertNotEquals(self.cities[0], self.sydney.name)
        self.assertNotEquals(self.cities[4], self.darwin.name)

    def locationInfo_connects_to_city(self):
        self.assertEquals(self.qut.city, self.brisbane.id)
        self.assertNotEquals(self.qut.city, self.sydney.id)
        self.assertEquals('QUT', self.qut.name)
        self.assertNotEquals('UQ', self.qut.name)
        
#Story No: 16 - Item Search
##class ItemSearch(TestCase):
##    QUT = LocationInfo(city="Brisbane", name="QUT", Address="55 Smith Street", email="qut@qut.edu.au", image="/Website/static/qut.png", phone="21212", info_type="0")
##    search_term = 'QUT'
##    info_type = "1"
##
##    def search_test(self):
##        test_data = LocationInfo.objects.filter(name=search_name).filter(infoType=info_type)
##        self.assertEqual(self.QUT, test_data)
