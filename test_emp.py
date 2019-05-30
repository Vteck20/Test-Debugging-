import unittest
from employee import employee

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass")

    def setUp(self):
        print('setUp')
        self.emp_1 = employee("Jeron","Lloyd",50000)
        self.emp_2 = employee("Ozni","Blan",60000)
    
    def tearDown(self):
        print("tearDown\n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email, "Jeron.Lloyd@gmail.com")
        self.assertEqual(self.emp_2.email, "Ozni.Blan@gmail.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Lloyd@gmail.com")
        self.assertEqual(self.emp_2.email, "Jane.Blan@gmail.com")

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Jeron Lloyd")
        self.assertEqual(self.emp_2.fullname, "Ozni Blan")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Lloyd")
        self.assertEqual(self.emp_2.fullname, "Jane Blan")
    
    def test_apply_raise(self):
        print("test_apply_raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)



if __name__ == "__main__":
    unittest.main()