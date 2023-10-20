from pillow_heif import register_heif_opener
from PIL import Image
import os

images_path = r"C:\\Users\\vshra\Downloads\Dataset-20231015T065504Z-001\Dataset"

register_heif_opener()

heic_list = []
for image in os.listdir(images_path):
    if image.split(".")[1].lower() == "heic":
        heic_list.append(image)

# print(len(heic_list))

for photo in heic_list:
    temp_img = Image.open(os.path.join(images_path, photo))
    if photo.split(".")[1] == "HEIC":
        jpg_photo = photo.replace("HEIC", "jpg")
    else:
        jpg_photo = photo.replace("heic", "jpg")
    temp_img.save(jpg_photo)
