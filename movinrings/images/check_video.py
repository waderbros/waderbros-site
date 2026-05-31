
import cv2
import os

video_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/マイムービー 7.mov'
output_gif = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/mymovie-7.gif'

cap = cv2.VideoCapture(video_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Original: {width}x{height}")

# ターゲットサイズ (既存GIFの比率 422:514 に合わせる)
# 横幅を 280px (CSSでの表示サイズ) にする場合
target_width = 280
target_height = int(target_width * (514 / 422))
print(f"Target: {target_width}x{target_height}")
