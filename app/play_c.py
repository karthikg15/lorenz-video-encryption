import cv2
import os
import natsort  # Install this package if not already installed

def make_video():
    try:
        os.chdir(r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\samples")
        image_folder = r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\encrypted_images"
        video_name = 'encrypted_video.avi'

        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
        if not images:
            print("No images found in the specified folder.")
            return

        images = natsort.natsorted(images)  # Natural sorting

        frame = cv2.imread(os.path.join(image_folder, images[0]))
        if frame is None:
            print("Error reading the first image.")
            return

        height, width, layers = frame.shape
        video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 40, (width, height))

        for image in images:
            frame = cv2.imread(os.path.join(image_folder, image))
            if frame is None:
                print(f"Error reading image {image}.")
                continue
            video.write(frame)

        video.release()
        cv2.destroyAllWindows()
        print(f"Video saved as {video_name}.")

    except Exception as e:
        print(f"An error occurred: {e}")

make_video()
