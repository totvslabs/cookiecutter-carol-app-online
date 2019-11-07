"""
Test Suite for {{cookiecutter.project_slug}}
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from src import {{cookiecutter.project_slug}}


class TestNlpApi(unittest.TestCase):
    def setUp(self):
        """Setup all variables mocks and things for all test steps
        """
        return super().setUp()

    def test_hello_world(self):
        """Test the /api/hello_world endpoint
        """
        return_value = {{cookiecutter.project_slug}}.hello_world()
        self.assertDictEqual(return_value, {'message': 'Hello World'})

    def test_main(self):
        """Test if OnLineAPI is executed correctly
        """
        with patch.object({{cookiecutter.project_slug}}, "__name__", "__main__"):
            {{cookiecutter.project_slug}}.application.run = MagicMock()
            {{cookiecutter.project_slug}}.main()
            {{cookiecutter.project_slug}}.application.run.assert_called_with(debug=True)

    def tearDown(self):
        """Undo all things setted up for those tests
        """
        return super().tearDown()
