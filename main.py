import os
from src.image_finder import ImageFinder
from src.job_generator import JobGenerator
from src.job_writer import JobWriter

def main():
    try:
        # Initialize components
        image_finder = ImageFinder()
        current_dir = os.getcwd()
        
        # Find images
        image_files = image_finder.find_images(current_dir)
        
        if not image_files:
            print("No image files found in the current directory.")
            return
        
        # Select source and target images
        source_path = image_files[0]
        target_paths = image_files[1:]
        
        if not target_paths:
            print("Need at least two images: one source and one target.")
            return
        
        # Generate jobs
        jobs = JobGenerator.create_jobs(source_path, target_paths)
        
        # Write jobs to file
        JobWriter.write_jobs(jobs)
        
        # Print summary
        print(f"Created jobs.json with {len(jobs)} jobs")
        print(f"Source image: {source_path}")
        print(f"Number of target images: {len(target_paths)}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()