import unittest
from data.solution import JsonOps
print('test')
class TestUser(unittest.TestCase):
    object1 = JsonOps('data_2.json')
    def test_type_loaded_data(self):
       returned_type = type(self.object1.json_file())
       self.assertEqual(returned_type, dict)

    def test_generated_schema(self):
       returned_type = type(self.object1.json_file())
       self.assertEqual(returned_type, dict)

if __name__ == '__main__':
    unittest.main()