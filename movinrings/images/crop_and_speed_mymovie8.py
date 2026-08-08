import cv2
import numpy as np
import os
import subprocess

dir_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/'
input_path = os.path.join(dir_path, 'mymovie-8.mp4')
temp_path = os.path.join(dir_path, 'mymovie-8-temp.mp4')
output_path = os.path.join(dir_path, 'mymovie-8-0.6x.mp4')

cap = cv2.VideoCapture(input_path)
orig_fps = cap.get(cv2.CAP_PROP_FPS)  # 59.94
target_fps = orig_fps * 0.6  # 35.964

w_out, h_out = 422, 514

# 角丸マスク (422 x 514, radius=55, x1=56, y1=44, x2=412, y2=510)
mask_rounded = np.zeros((h_out, w_out), dtype=np.uint8)
r = 55
x1_m, y1_m, x2_m, y2_m = 56, 44, 412, 510

cv2.rectangle(mask_rounded, (x1_m+r, y1_m), (x2_m-r, y2_m), 255, -1)
cv2.rectangle(mask_rounded, (x1_m, y1_m+r), (x2_m, y2_m-r), 255, -1)
cv2.circle(mask_rounded, (x1_m+r, y1_m+r), r, 255, -1)
cv2.circle(mask_rounded, (x2_m-r, y1_m+r), r, 255, -1)
cv2.circle(mask_rounded, (x1_m+r, y2_m-r), r, 255, -1)
cv2.circle(mask_rounded, (x2_m-r, y2_m-r), r, 255, -1)

mask_3ch = cv2.cvtColor(mask_rounded, cv2.COLOR_GRAY2BGR) / 255.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(temp_path, fourcc, target_fps, (w_out, h_out))

# 上部の空きをさらに削り時計の枠をさらに高位置へ持ち上げ (x=535, y=370, w=210, h=275)
# 歪みゼロ: 210 / 275 = 0.7636 (356 / 466 に100%一致)
x_start = 535
y_start = 370
w_crop = 210
h_crop = 275

while True:
    ret, frame = cap.read()
    if not ret:
        break
    crop = frame[y_start:y_start+h_crop, x_start:x_start+w_crop]
    resized_content = cv2.resize(crop, (356, 466), interpolation=cv2.INTER_LANCZOS4)

    canvas = np.zeros((h_out, w_out, 3), dtype=np.uint8)
    canvas[44:44+466, 56:56+356] = resized_content

    final_frame = (canvas * mask_3ch).astype(np.uint8)
    out.write(final_frame)

cap.release()
out.release()
print(f"Watch frame shifted EVEN HIGHER video generated: {w_out}x{h_out} at {target_fps:.3f}fps")

# Safari / Apple 100% 互換エンコード (H.264 yuv420p)
cmd = [
    'avconvert',
    '--source', temp_path,
    '--preset', 'PresetHighestQuality',
    '--output', output_path,
    '--replace'
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("avconvert result:", res.stdout, res.stderr)

if os.path.exists(output_path):
    print(f"Shifted EVEN HIGHER watch video created successfully: {output_path}")
