import os
from pathlib import Path
from typing import List

class ImageFinder:
    def __init__(self):
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}
    
    def find_images(self, directory: str) -> List[str]:
        """Find all image files in the specified directory."""
        image_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if Path(file).suffix.lower() in self.image_extensions:
                    image_files.append(os.path.join(root, file))
        return image_files