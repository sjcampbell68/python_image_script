import os
import json
from pathlib import Path

def find_image_files(directory):
    # Common image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}
    
    image_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix.lower() in image_extensions:
                image_files.append(os.path.join(root, file))
    return image_files

def create_facefusion_job(source_path, target_paths):
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

def main():
    # Get the current directory
    current_dir = os.getcwd()
    
    # Find all image files
    image_files = find_image_files(current_dir)
    
    if not image_files:
        print("No image files found in the current directory.")
        return
    
    # Use the first image as source (you can modify this logic)
    source_path = image_files[0]
    target_paths = image_files[1:]
    
    if not target_paths:
        print("Need at least two images: one source and one target.")
        return
    
    # Create jobs
    jobs = create_facefusion_job(source_path, target_paths)
    
    # Save to jobs.json
    with open('jobs.json', 'w') as f:
        json.dump(jobs, f, indent=2)
    
    print(f"Created jobs.json with {len(jobs)} jobs")
    print(f"Source image: {source_path}")
    print(f"Number of target images: {len(target_paths)}")

if __name__ == "__main__":
    main()