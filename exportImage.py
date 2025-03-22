import os
from pdf2image import convert_from_path

DPI: int = 200  # Default: 200
POPPLER_PATH: str = "./install/poppler/Library/bin"
folder_path: str = "./originalFile"

target_path: str = "./result"
if not os.path.isdir(target_path):
    os.mkdir(target_path)

all_items = os.listdir(folder_path)

file_list = []

for item in all_items:
    pdf_file_path: str = os.path.join(folder_path, item)
    if os.path.isfile(pdf_file_path):
        file_list.append(item) 
    pages = convert_from_path(pdf_path=pdf_file_path, dpi=DPI, poppler_path=POPPLER_PATH)

    for page_index, page in enumerate(pages):
        new_page_index: str = str(page_index + 1).zfill(4)
        export_folder: str=f"{target_path}/{os.path.splitext(item)[0]}"
        if not os.path.isdir(export_folder):
            os.mkdir(export_folder)
        image_path_name: str = f"{export_folder}/image_{new_page_index}.jpg"
        page.save(fp=image_path_name, format="JPEG")

print("Finished")

    