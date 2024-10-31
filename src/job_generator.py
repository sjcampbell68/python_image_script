import os
from typing import List, Dict

class JobGenerator:
    @staticmethod
    def create_jobs(source_path: str, target_paths: List[str]) -> List[Dict]:
        """Create FaceFusion jobs for the given source and target images."""
        jobs = []
        for target_path in target_paths:
            job = {
                "source_path": source_path,
                "target_path": target_path,
                "output_path": f"output_{os.path.basename(target_path)}",
                "frame_processors": ["face_swapper"],
                "face_selector_mode": "reference",
                "face_mask_types": ["box"],
                "face_mask_blur": 0.3,
                "face_mask_padding": 0.0
            }
            jobs.append(job)
        return jobs