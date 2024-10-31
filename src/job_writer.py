import json
from typing import List, Dict

class JobWriter:
    @staticmethod
    def write_jobs(jobs: List[Dict], output_file: str = 'jobs.json') -> None:
        """Write jobs to a JSON file."""
        with open(output_file, 'w') as f:
            json.dump(jobs, f, indent=2)