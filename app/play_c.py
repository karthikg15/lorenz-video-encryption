import cv2
import os

def make_video():
    os.chdir(r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\samples")
    image_folder = r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\encrypted_images"
    video_name = 'encrypted_video.avi'

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 1, (width,height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()