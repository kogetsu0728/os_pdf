import glob
import os
import re
from PIL import Image
from reportlab.pdfgen import canvas

def get_image_dirs(parent_dir):
    pattern = re.compile(r'^OSⅠ第\d+回$')

    image_dirs = list()
    for sub_dir in os.listdir(parent_dir):
        if pattern.match(sub_dir):
            image_dirs.append(os.path.join(parent_dir, sub_dir))

    return image_dirs

def get_slide_number(image_name):
    match = re.search(r'(\d+)\.PNG', image_name)

    if match:
        return int(match.group(1))

    return -1

def images_to_pdf(image_files, pdf_name):
    canv = canvas.Canvas(pdf_name)

    for image_file in image_files:
        image_width, image_height = Image.open(image_file).size

        canv.setPageSize((image_width, image_height))
        canv.drawImage(image_file, 0, 0, width=image_width, height=image_height)

        canv.showPage()

    canv.save()
    print(f"{pdf_name}を作成したよ! :)")

def main():
    parent_dir = "./path/to/parent_dir"
    image_dirs = get_image_dirs(parent_dir)

    for image_dir in image_dirs:
        image_files = glob.glob(os.path.join(image_dir, "スライド*.PNG"))
        image_files.sort(key=get_slide_number)

        pdf_name = os.path.join(image_dir, "merged.pdf")
        images_to_pdf(image_files, pdf_name)

if __name__ == '__main__':
    main()
