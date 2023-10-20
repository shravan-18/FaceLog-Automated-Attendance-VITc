import os
import time
import uuid
import cv2

base_dir = "D:\VIT Material\VIT material\Projects\FaceRecognition-Attendance"


def capture_images(IMAGES_PATH):
    number_images = 30
    cap = cv2.VideoCapture(0)
    for imgnum in range(number_images):
        print("Collecting image {}".format(imgnum + 1))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, f"{str(uuid.uuid1())}.jpg")
        cv2.imwrite(imgname, frame)
        cv2.imshow("frame", frame)
        time.sleep(0.5)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    print("Images Captured!")
    cap.release()
    cv2.destroyAllWindows()


def check_person():
    choice = int(input("Are you capturing the image of a new person - (0/1)?\n"))
    try:
        if choice:
            print("New Person...")
            name = input("Enter your name: ")

            # Specify the path and name of the new folder
            folder_path = os.path.join(base_dir, "images")
            folder_name = name

            # Combine the path and folder name to create the full folder path
            new_folder_path = os.path.join(folder_path, folder_name)

            # Check if the folder already exists before creating it
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
                print(
                    f"Folder '{folder_name}' created successfully at '{new_folder_path}'"
                )
            else:
                print(f"Folder '{folder_name}' already exists at '{new_folder_path}'")

            capture_images(new_folder_path)

        else:
            print("Capturing existing user's face again...")
            name = input("Enter your name: ")
            if name not in os.listdir(os.path.join(base_dir, "images")):
                print("Sorry, your existing data could not be found!")
                exit()
            else:
                person_path = os.path.join(base_dir, "images", name)
                capture_images(person_path)

    except ValueError:
        print("Invalid Input")

    except Exception as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    check_person()
