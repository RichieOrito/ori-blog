from app.models import Blog
from app import db
import unittest

class BlogModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Blog class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_blog = Blog(id=254,title_blog='Tech',description='we need it')

    def tearDown(self):
        Blog.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
        

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.id,254)
        self.assertEquals(self.new_blog.title_blog,'Tech')
        self.assertEquals(self.new_blog.description,'we need it')


