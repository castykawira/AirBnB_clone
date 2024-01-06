#!/usr/bin/python3
"""Test cases BaseModel class"""
import unittest
import os
import models
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """BaseModel class test cases"""

   def test_basic(self):
        """
        Tests basic imputs for the BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                         ["ALX", 89])
        
   def test_inequality_of_two_different_objects_ids(self):
        """Inequality of two different objects ids"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_inequality_of_two_instances_of_BaseModel(self):
        """Inequality of two instances of BaseModel"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1, base_model2)

    def test_id_is_string(self):
        """Check if the id is string"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_base_model_originates_from_object_class(self):
        """Check if the BaseModel originates from object class"""
        self.assertIsInstance(BaseModel(), object)

    def test_printing_instance_equals_string_format(self):
        """Check if the printing the instance of BaseModel equals
        “[<class name>] (<self.id>) <self.__dict__>” string format"""
        base_model = BaseModel()
        expected_str = (
                f"[{base_model.__class__.__name__}] "
                f"({base_model.id}) {base_model.__dict__}"
                )
        self.assertEqual(str(base_model), expected_str)

    def test_inequality_of_greater_than_two_objects_ids(self):
        """Inequality of greater than 2 different objects ids"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        base_model3 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)
        self.assertNotEqual(base_model2.id, base_model3.id)
        self.assertNotEqual(base_model1.id, base_model3.id)

    def test_created_time_is_always_less_than_current_time(self):
        """Check if the created time is always less than the current time"""
        base_model = BaseModel()
        self.assertLess(base_model.created_at, datetime.now())

    def test_id_is_uuid4_string(self):
        """Ensure id is a uuid4 string (len == 36)"""
        base_model = BaseModel()
        self.assertEqual(len(str(base_model.id)), 36)

    def test_updated_at_after_save_is_greater_than_old_updated_at(self):
        """Check that the updated_at after using the save method
        is greater than the old updated_at"""
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertGreater(base_model.updated_at, old_updated_at)

    def test_to_dict_method_returns_correct_keys_and_values(self):
        """Check if to_dict method returned a dictionary
        that has the correct keys and values"""
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_created_at_and_updated_at_are_instances_of_datetime(self):
        """Check if created_at, and Updated_at are instances of datetime"""
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_to_dict_method_returns_dictionary(self):
        """Test the to_dict method"""
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)


if __name__ == '__main__':
    unittest.main()
