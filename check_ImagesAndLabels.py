import os

curr_dir = os.getcwd()
images_dir = os.path.join(curr_dir, "Dataset", "images")
labels_dir = os.path.join(curr_dir, "Dataset", "labels")

print(len(os.listdir(images_dir)), len(os.listdir(labels_dir)))

images = []

for image_name in os.listdir(images_dir):
    images.append(image_name.split(".")[0])

print(len(images))

for label in os.listdir(labels_dir):
    if label.split(".")[0] in images:
        images.remove(label.split(".")[0])

print(images)
