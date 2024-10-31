import unittest
from src.job_generator import JobGenerator

class TestJobGenerator(unittest.TestCase):
    def test_create_jobs(self):
        source = "source.jpg"
        targets = ["target1.jpg", "target2.jpg"]
        
        jobs = JobGenerator.create_jobs(source, targets)
        
        self.assertEqual(len(jobs), 2)
        self.assertEqual(jobs[0]["source_path"], source)
        self.assertEqual(jobs[0]["target_path"], targets[0])
        self.assertTrue("face_swapper" in jobs[0]["frame_processors"])