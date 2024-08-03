# PNG Exif Metadata Remover

## Description
This Python script recursively removes metadata (including EXIF data) from all PNG files in a specified directory and its subdirectories. It uses multiprocessing to enhance performance and provides a progress bar to track the operation.

## Features
- Recursively processes all PNG files in a directory and its subdirectories
- Removes metadata from PNG files
- Uses multiprocessing for improved performance
- Displays a progress bar during execution
- Provides a summary of processed files, errors, and unchanged files
- Skips files that don't have metadata, optimizing processing time

## Requirements
- Python 3.6+
- Pillow
- tqdm

## Installation

1. Clone this repository:
   git clone https://github.com/undeadx1/ExifRemover.git
   cd png-metadata-remover

2. Install the required packages:
   pip install -r requirements.txt

## Usage

1. Place the script in the directory containing the PNG files you want to process (or any parent directory).

2. Run the script:
   python png_metadata_remover.py

3. The script will process all PNG files in the current directory and its subdirectories. A progress bar will show the status of the operation.

4. After completion, a summary will be displayed showing the number of processed files, errors, and unchanged files.

## Output Example
Processing 100 PNG files.
Processing: 100%|██████████| 100/100 [00:05<00:00, 18.73it/s]

Task completed:
- Files processed: 75
- Errors occurred: 2
- No changes: 23

Error occurred (path/to/file1.png): [Error message]
Error occurred (path/to/file2.png): [Error message]

## Caution
- This script modifies files in-place. It's recommended to backup your files before running the script.
- While the script is designed to only remove metadata, it's always a good practice to test it on a small set of non-critical files first.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/png-metadata-remover/issues) if you want to contribute.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Pillow](https://python-pillow.org/) for image processing capabilities
- [tqdm](https://github.com/tqdm/tqdm) for the progress bar functionality
