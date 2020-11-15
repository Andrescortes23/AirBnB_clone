#!/usr/bin/python3
"""
Unittest City class
"""
import unittest
import pep8
import sys
import os
from datetime import datetime
from models import city
from models.city import City


class TestPep8B(unittest.TestCase):
    """ Test pep8 style validation """

    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/city.py'
        file2 = 'tests/test_models/test_city.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)


class BaseModelclassTests(unittest.TestCase):
    """ Test Case for base_model moudle """

    def setUp(self):
        """ Create instance global  """
        self.ins0 = City()
        self.ins1 = City()

    def tearDown(self):
        """ Clean All test case """
        pass

    def test_instance(self):
        """ Test Case to check instance  """
        self.assertIsInstance(self.ins0, City)
        self.assertIsInstance(self.ins1, City)

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/city.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/city.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/city.py', os.X_OK)
        self.assertTrue(exe)

    def test_id(self):
        """
        Test id of instances
        instance id will be not equal
        type, will be str
        """
        self.assertNotEqual(self.ins0.id, self.ins1.id)
        self.assertEqual(type(self.ins0.id), str)
        self.assertEqual(type(self.ins1.id), str)

    def test_datetime_save(self):
        """ Test datetime to compare format """
        cre = self.ins0.created_at
        self.ins0.save()
        up = self.ins0.updated_at
        self.assertEqual(type(cre), datetime)
        self.assertEqual(type(up), datetime)
        self.assertNotEqual(cre, up)  # time create and update are diff

    def test_to_dict(self):
        """ The value return by to_dict the same value """
        dateform = '%Y-%m-%dT%H:%M:%S.%f'
        dic = self.ins0.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(dic['created_at'],
                         self.ins0.created_at.strftime(dateform))
        self.assertEqual(dic['updated_at'],
                         self.ins0.updated_at.strftime(dateform))

    def test_name_stid_str(self):
        """ Test data type intro. Will be str """
        namestr = self.ins0.name
        st_idstr = self.ins0.state_id
        self.assertEqual(type(namestr), str)
        self.assertEqual(type(st_idstr), str)


if __name__ == '__main__':
    unittest.main()
