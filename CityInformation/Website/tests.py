from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import College
from Website.models import City
from .urls import *
from django.db import IntegrityError

# To Run tests:
# python manage.py test Website.tests

# Story: S03 - Log In
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
class MenuNavigation(TestCase):
    urls = [
        "http://127.0.0.1:8000/Website/",
        "http://127.0.0.1:8000/Website/register",
        "http://127.0.0.1:8000/logout",
        "http://127.0.0.1:8000/login",
    ]

    def test_navigation_works(self):
        pass

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
