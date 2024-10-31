# FaceFusion Job Generator

A Python tool to generate FaceFusion 3.x compatible job files from a directory of images.

## Features

- Automatically scans directories for image files
- Supports common image formats (jpg, jpeg, png, webp, bmp)
- Generates FaceFusion 3.x compatible job configurations
- Modular and testable design

## Usage

1. Place your images in the project directory
2. Run the script:
   ```bash
   python main.py
   ```
3. A `jobs.json` file will be generated with FaceFusion configurations

## Testing

Run the tests using:
```bash
python -m pytest tests/
```

## Project Structure

- `src/` - Source code modules
  - `image_finder.py` - Image file detection
  - `job_generator.py` - FaceFusion job creation
  - `job_writer.py` - JSON output handling
- `tests/` - Unit tests
- `main.py` - Main application entry point