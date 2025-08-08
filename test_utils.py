import os
from app.utils import extract_text_from_file

APP_FOLDER = "app"

def test_text_extraction():
    for filename in os.listdir(APP_FOLDER):
        file_path = os.path.join(APP_FOLDER, filename)

        if not os.path.isfile(file_path):
            continue

        if not filename.lower().endswith(('.pdf', '.docx', '.txt')):
            continue  

        try:
            with open(file_path, "rb") as f:
                text = extract_text_from_file(f, filename)
                print(f"\n----- {filename} -----")
                print(text[:1000])  
        except Exception as e:
            print(f" Failed to process {filename}: {e}")

if __name__ == "__main__":
    test_text_extraction()
