import datetime

from django.utils import timezone
from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User


class QuestionModelTests(TestCase):

    def test_was_published_date(self):

        time = timezone.now()
        # create a user
        user =  User.objects.create_user('HyeRiChang', 'anh.nguyentu3110@gmail.com', 'joinpassword')
        # create a post
        self.post = Post.objects.create(title='HyeRiChang', author=user, text='I love cat')
        # update post
        self.post.published(time)
        self.assertIs(self.post.published_date, time)
