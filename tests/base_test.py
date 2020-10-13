"""
This file will contain a class which will set up
a new blank database for each test
"""


from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    """
    This class will setup a testing class
    """
    def setUp(self):
        """
        This class is called before every test.
         - make sure database exist
         - get a test client
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()

        # get a test client
        self.app = app.test_client()
        self.app_content = app.app_context()

    def tearDown(self):
        """
        This class is called after each test
        - make a the database blank
        """

        with app.app_context():
            db.session.remove()
            db.drop_all()  # remove all tables
