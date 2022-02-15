from turtle import title
from app.models import Comment
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Comment class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_comment = Comment(id=1,comment='awesome')

    def tearDown(self):
        Comment.query.delete()


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.id,1)
        self.assertEquals(self.new_comment.comment,'awesome')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_review_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(254)
        self.assertTrue(len(got_comments) == 0)