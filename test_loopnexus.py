# test_loopnexus.py
"""
Tests for LoopNexus module.
"""

import unittest
from loopnexus import LoopNexus

class TestLoopNexus(unittest.TestCase):
    """Test cases for LoopNexus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LoopNexus()
        self.assertIsInstance(instance, LoopNexus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LoopNexus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
