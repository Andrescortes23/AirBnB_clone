#!/usr/bin/python3
"""
Amenity class test module
"""
import os
import pep8
import sys
import unittest
from datetime import datetime
from models import amenity
from models.amenity import Amenity


class TestPep8(unittest.TestCase):
    """ Validates PEP8 style """

    def test_pep8(self):
        """ Validates PEP8 style conformance """

        style = pep8.StyleGuide(quiet=True)
        f1 = 'models/amenity.py'
        f2 = 'tests/test_models/test_amenity.py'
        res = style.check_files([f1, f2])
        self.assertEqual(res.total_errors, 0, "Code has style errors.")


class TestDocs(unittest.TestCase):
    """ Validates docstring """

    def test_module_doc(self):
        """ Validates module doc """

        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """ Validates class doc """

        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """ Validates methods doc """

        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)


class BaseModelclassTests(unittest.TestCase):
    """ Test Case for base_model moudle """

    def setUp(self):
        """ Create instance global  """
        self.ins0 = Amenity()
        self.ins1 = Amenity()

    def tearDown(self):
        """ Clean All test case """
        pass

    def test_instance(self):
        """ Test Case to check instance  """
        self.assertIsInstance(self.ins0, Amenity)
        self.assertIsInstance(self.ins1, Amenity)

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/amenity.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/amenity.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/amenity.py', os.X_OK)
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

    def test_name_str(self):
        """ Test data type intro. Will be str """
        namestr = self.ins0.name
        self.assertEqual(type(namestr), str)


if __name__ == '__main__':
    unittest.main()
