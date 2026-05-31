
import cv2
from PIL import Image
import numpy as np

video_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/マイムービー 7.mov'
output_gif = '/Users/MasaWaderbros-site/movinrings/images/mymovie-7.gif'
# 上記パスの誤字修正
output_gif = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/mymovie-7.gif'

cap = cv2.VideoCapture(video_path)
frames = []
count = 0
while True:
    ret, frame = cap.read()
    if not ret: break # 全フレーム処理
    
    # BGR -> RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    
    # センタークロップ + リサイズ
    # 動画(1280x720)を縦長(280x341)にするため、まず高さを720に合わせるクロップ
    # 720 / 341 * 280 = 591
    crop_width = int(720 * (280 / 341))
    left = (1280 - crop_width) // 2
    img = img.crop((left, 0, left + crop_width, 720))
    img = img.resize((280, 341), Image.Resampling.LANCZOS)
    
    frames.append(img)

frames[0].save(
    output_gif,
    save_all=True,
    append_images=frames[1:],
    duration=1000,
    loop=0
)
print(f"Saved to {output_gif}")
