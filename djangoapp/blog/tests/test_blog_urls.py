from django.urls import reverse
from .test_blog_base import BlogTestBase

class BlogURLsTests(BlogTestBase):
    def test_blog_home_url_is_correct(self):
        url = reverse("blog:index-blog")
        self.assertEqual(url, "/blog/")

    def test_blog_tag_url_is_correct(self):
        tag_obj = self.make_tag()
        url = reverse("blog:tag", kwargs={"slug": tag_obj.slug})
        self.assertEqual(url, "/blog/tag/test-tag")

    def test_blog_category_url_is_correct(self):
        category_obj = self.make_category()
        url = reverse("blog:tag", kwargs={"slug": category_obj.slug})
        self.assertEqual(url, "/blog/tag/test-category")

    def test_blog_post_url_is_correct(self):
        post_obj = self.make_post()
        url = reverse("blog:post", kwargs={"slug": post_obj.slug})
        self.assertEqual(url, "/blog/post/test-post")