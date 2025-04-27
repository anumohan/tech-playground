import unittest
import json
from app import app


class FlaskAppTests(unittest.TestCase):

    # Set up test client
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_home(self):        
        print('-------------- in test --------------')
        response = self.client.get('/')        

        print(dir(response))


        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Flask is working')
        self.assertEqual(response.get_json(), None)

        #self.assertEqual(response.get_json(), {"message": "Welcome to Flask!"})
        #self.assertIsNone(result, "Expected None when condition is false")




if __name__ == '__main__':
    unittest.main()

'''
calling test 
python -m unittest discover -s tests

'''



import os
os.environ['DATABASE_URL'] = 'sqlite://'

