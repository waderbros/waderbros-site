
import cv2

video_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/マイムービー 7.mov'
output_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/mymovie-7.mp4'

cap = cv2.VideoCapture(video_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 動画をmp4vコーデックで保存
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret: break
    out.write(frame)

cap.release()
out.release()
print(f"Saved to {output_path}")
