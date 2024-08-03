import os
import multiprocessing
from PIL import Image
from tqdm import tqdm

def has_metadata(img):
    return len(img.info) > 0

def process_image(file_path):
    try:
        with Image.open(file_path) as img:
            if has_metadata(img):
                data = list(img.getdata())
                img_without_exif = Image.new(img.mode, img.size)
                img_without_exif.putdata(data)
                img_without_exif.save(file_path, "PNG")
                return f"Metadata removed: {file_path}"
    except Exception as e:
        return f"Error occurred ({file_path}): {str(e)}"

def remove_exif_from_png(folder_path):
    png_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.png'):
                png_files.append(os.path.join(root, filename))

    print(f"Processing {len(png_files)} PNG files.")

    with multiprocessing.Pool() as pool:
        results = list(tqdm(pool.imap(process_image, png_files), total=len(png_files), desc="Processing"))

    processed = sum(1 for r in results if r and r.startswith("Metadata removed"))
    errors = sum(1 for r in results if r and r.startswith("Error occurred"))

    print(f"\nTask completed:")
    print(f"- Files processed: {processed}")
    print(f"- Errors occurred: {errors}")
    print(f"- No changes: {len(png_files) - processed - errors}")

    # Print error messages
    for result in results:
        if result and result.startswith("Error occurred"):
            print(result)

if __name__ == '__main__':
    current_directory = os.getcwd()
    remove_exif_from_png(current_directory)