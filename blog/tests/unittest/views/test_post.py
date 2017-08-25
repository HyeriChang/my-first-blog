from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
from django.test import Client
from django.utils import timezone
from django.urls import reverse


def check_text_in_string(content, text):
    result = False
    result = text in str(content)
    return result

class ViewPostTestClass(TestCase):

    def setUp(self):
        #Setup run before every test method.
        #Todo
        # create one user
        self.user = User.objects.create_user('TuAnh', 'anh.nt@gmail.com', 'joinning')
        # create one post
        self.post1 = Post.objects.create(title='Summer', author=self.user,text='Holiday', published_date=timezone.now() - timezone.timedelta(days=1))
        # create one more post
        self.post2 = Post.objects.create(title='Winter', author=self.user,text='Sleep', published_date=timezone.now() - timezone.timedelta(days=1))
        self.client = Client()

    def tearDown(self):
        #Clean up run after every test method.

        # delete the created user

        pass
    def test_see_list_posts(self):
        # create a client test

        # use client makes a get request to '/'
        # take the response then check
        response = self.client.get('/')
        #   check status_code=200, ..
        # import pdb; pdb.set_trace()

        self.assertIs(response.status_code, 200)
        # import pdb; pdb.set_trace()
        #   check title post exists in response content
        self.assertIs(check_text_in_string(response.content, 'Summer'), True)

        #   check body post exists in response content

    def test_post_detail(self):

        response = self.client.get (reverse('post_detail', args=[self.post1.id]))
        self.assertIs(response.status_code, 200)
        self.assertIs(check_text_in_string(response.content, 'Summer'), True)
        self.assertIs(check_text_in_string(response.content, 'Holiday'), True)

    def test_create_post(self):

        # create client
        # client login with self.user
        # client post data: with data is {'title': '', 'text': ''}
        # validate response content is having post title, post text
        # response = c.post('/login/', {'username': self.user.username, 'password': 'joinning'})

        self.client.login(username=self.user.username, password='joinning')
        data = {'title': 'NewSummer','text': 'NewHoliday'}
        response = self.client.post(reverse('post_new'), data)
        self.assertEqual(response.status_code, 302)

    def test_edit_post(self):
        self.client.login(username=self.user.username, password='joinning')
        data = {'title': 'NewWinter', 'text': 'NewSleep'}
        response = self.client.post(reverse('post_edit', args= [self.post1.id]), data)
        self.assertEqual(response.status_code, 302)


    def test_comment(self):
        self.client.login(username=self.user.username, password='joinning')
        data = {'title': 'hinh', 'text': 'NewSleep'}
        response = self.client.post(reverse('comment', args= [self.post1.id]), data)
        self.assertEqual(response.status_code, 302)



