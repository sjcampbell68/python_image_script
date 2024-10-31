import unittest
from src.image_finder import ImageFinder
import os
import tempfile
from pathlib import Path

class TestImageFinder(unittest.TestCase):
    def setUp(self):
        self.finder = ImageFinder()
        self.temp_dir = tempfile.mkdtemp()
        
    def test_find_images(self):
        # Create test images
        test_files = ['test1.jpg', 'test2.png', 'test3.txt']
        for file in test_files:
            Path(os.path.join(self.temp_dir, file)).touch()
            
        images = self.finder.find_images(self.temp_dir)
        self.assertEqual(len([f for f in images if f.endswith(('.jpg', '.png'))]), 2)
        
    def tearDown(self):
        # Cleanup
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)