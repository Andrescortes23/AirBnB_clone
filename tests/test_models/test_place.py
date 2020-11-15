#!/usr/bin/python3
"""
Unittest Place class
"""
import unittest
import pep8
import sys
import os
from datetime import datetime
from models import place
from models.place import Place


class TestPep8B(unittest.TestCase):
    """ Test pep8 style validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/place.py'
        file2 = 'tests/test_models/test_place.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)


class PlaceclassTests(unittest.TestCase):
    """ Test Case for place module """

    def setUp(self):
        """ Create instance global  """
        self.ins0 = Place()
        self.ins1 = Place()

    def tearDown(self):
        """ Clean All test case """
        pass

    def test_instance(self):
        """ Test Case to check instance  """
        self.assertIsInstance(self.ins0, Place)
        self.assertIsInstance(self.ins1, Place)

    def test_permissions(self):
        """test read-write-execute permissions"""
        read = os.access('models/place.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/place.py', os.W_OK)
        self.assertTrue(write)
        exe = os.access('models/place.py', os.X_OK)
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
        """ The dict return is the same """
        dateform = '%Y-%m-%dT%H:%M:%S.%f'
        dic = self.ins0.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)
        self.assertEqual(dic['created_at'],
                         self.ins0.created_at.strftime(dateform))
        self.assertEqual(dic['updated_at'],
                         self.ins0.updated_at.strftime(dateform))

    def test_city_id_str(self):
        """ Test type of date. Will be str"""
        idcitystr = self.ins0.city_id
        self.assertEqual(type(idcitystr), str)

    def test_user_id_str(self):
        """ Test type of date. Will be str"""
        iduserstr = self.ins0.user_id
        self.assertEqual(type(iduserstr), str)

    def test_name_str(self):
        """ Test type of date. Will be str"""
        namestr = self.ins0.name
        self.assertEqual(type(namestr), str)

    def test_description_str(self):
        """ Test type of date. Will be str"""
        descstr = self.ins0.description
        self.assertEqual(type(descstr), str)

    def test_int(self):
        """ Test type of date. Will be int"""
        roomint = self.ins0.number_rooms
        bathint = self.ins0.number_bathrooms
        guestint = self.ins0.max_guest
        priceint = self.ins0.price_by_night
        self.assertEqual(type(roomint), int)
        self.assertEqual(type(bathint), int)
        self.assertEqual(type(guestint), int)
        self.assertEqual(type(priceint), int)

    def test_amenity_ids_str(self):
        """ Test type of date. Will be list"""
        idamenstr = self.ins0.amenity_ids
        self.assertEqual(type(idamenstr), list)

    def test_float(self):
        """ Test type of date. Will be float"""
        latitudeint = self.ins0.latitude
        longitudeint = self.ins0.longitude
        self.assertEqual(type(latitudeint), float)
        self.assertEqual(type(longitudeint), float)


if __name__ == '__main__':
    unittest.main()
