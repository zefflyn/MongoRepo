# test_mongorepo.py
"""
Tests for MongoRepo module.
"""

import unittest
from mongorepo import MongoRepo

class TestMongoRepo(unittest.TestCase):
    """Test cases for MongoRepo class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MongoRepo()
        self.assertIsInstance(instance, MongoRepo)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MongoRepo()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
