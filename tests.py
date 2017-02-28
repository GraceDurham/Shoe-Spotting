import unittest

import server

import model


class ServerTests(unittest.TestCase):
    """Tests for my shoe site."""

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("Welcome to Shoe Spotting", result.data)

    def test_has_not_registered_yet(self):
        result = self.client.get('/register')
        self.assertIn("Register", result.data)
        self.assertNotIn("Welcome to Shoe Spotting", result.data)


    def test_registered(self):
        result = self.client.post("/register",
                                  data={'name': "Grace", 'email': "grace@gmail.com"},
                                  follow_redirects=True)
        self.assertNotIn("Register", result.data)
        self.assertIn("Welcome to Shoe Spotting", result.data)
        # FIXME: check that once we log in we see party details--but not the form!
    

# class PartyTestsDatabase(unittest.TestCase):
#     """Flask tests that use the database."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         # Get the Flask test client
#         self.client = app.test_client()

#         # Show Flask errors that happen during tests
#         app.config['TESTING'] = True

#         # Connect to test database
#         connect_to_db(app, "postgresql:///testdb")

#         # Create tables and add sample data
#         db.create_all()
#         example_data()

#     def tearDown(self):
#         """Do at end of every test."""

#         db.session.close()
#         db.drop_all()

#     def test_games(self):
#         """Test departments page."""

#         result = self.client.get("/games")
#         self.assertIn("Power Grid", result.data)


if __name__ == "__main__":
    unittest.main()