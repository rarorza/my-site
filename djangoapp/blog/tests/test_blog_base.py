from django.test import TestCase

from blog.models import Post, Tag, Category, User

class BlogTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_author(
        self,
        first_name="user",
        last_name="name",
        username="user",
        email="user@user.com",
        password="User*123",
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )
    
    def make_tag(self, name="test tag", slug="test-tag"):
        return Tag.objects.create(name=name, slug=slug)
    
    def make_category(self, name="test category", slug="test-category"):
        return Category.objects.create(name=name, slug=slug)
    
    def make_post(
            self,
            is_published=True,
            author_data=None,
            tag_data=None,
            category_data=None,
            title="test post",
            slug="test-post",
            excerpt="#" * 150,
            content="post content",
        ):

        if author_data is None:
            author_data = {}

        if category_data is None:
            category_data = {}

        if tag_data is None:
            tag_data = {}
        
        post = Post.objects.create(
            created_by=self.make_author(**author_data),
            category=self.make_category(**category_data),
            is_published=is_published,
            title=title,
            slug=slug,
            excerpt=excerpt,
            content=content,
        )
        
        tag = self.make_tag(**tag_data)
        post.tags.add(tag)

        return post