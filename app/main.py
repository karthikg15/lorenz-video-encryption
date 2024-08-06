import cv2
import os
import en_c, play_c

def FrameCapture(video_path, output_dir): 
    
    vidObj = cv2.VideoCapture(video_path) 
    if not vidObj.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    count = 0
    success = True

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    os.chdir(output_dir)
    print("Encoding the video...")
    while success: 
        success, image = vidObj.read()
        if not success:
            break
        if image is not None:
            name = f"frame{count}"
            frame_filename = f"frame{count}.jpg"
            cv2.imwrite(frame_filename, image)
            en_c.encryptionfn(image_path = f"C:\\Users\\zoro0\\Desktop\\chaoticmap\\Video_encryption\\generated_images\\{frame_filename}", 
                               frame_name= name) 
            count += 1
        else:
            print(f"Warning: Frame {count} is None, skipping...")

    # print(f"Extracted {count} frames from {video_path} to {output_dir}")
    play_c.make_video()
    print("Completed!!!")


if __name__ == '__main__': 
    video_path = r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\samples\waves.mp4"
    output_dir = r"C:\Users\zoro0\Desktop\chaoticmap\Video_encryption\generated_images"
    FrameCapture(video_path, output_dir)
    

    

