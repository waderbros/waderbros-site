import cv2
import numpy as np
import os
import subprocess

src_dir = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/'
dst_dir = '/Users/MasaWada2/Documents/GitHub/waderbros-site/metronomeandjam/images/'
os.makedirs(dst_dir, exist_ok=True)

# --- 1. iPhone 動画 (1.2倍用 超絶フルHD 560 x 1264px) ---
iphone_in = os.path.join(src_dir, 'マイムービー 10.mp4')
iphone_temp = os.path.join(dst_dir, 'temp_iphone.mp4')
iphone_out = os.path.join(dst_dir, 'metronomeandjam-iphone.mp4')

w_p_out, h_p_out = 560, 1264
w_phone, h_phone = 550, 1254
x_phone_off, y_phone_off = 5, 5

mask_phone = np.zeros((h_p_out, w_p_out), dtype=np.uint8)
r_p = 65
cv2.rectangle(mask_phone, (5+r_p, 5), (555-r_p, 1259), 255, -1)
cv2.rectangle(mask_phone, (5, 5+r_p), (555, 1259-r_p), 255, -1)
cv2.circle(mask_phone, (5+r_p, 5+r_p), r_p, 255, -1)
cv2.circle(mask_phone, (555-r_p, 5+r_p), r_p, 255, -1)
cv2.circle(mask_phone, (5+r_p, 1259-r_p), r_p, 255, -1)
cv2.circle(mask_phone, (555-r_p, 1259-r_p), r_p, 255, -1)
mask_phone_3ch = cv2.cvtColor(mask_phone, cv2.COLOR_GRAY2BGR) / 255.0

cap10 = cv2.VideoCapture(iphone_in)
fps10 = cap10.get(cv2.CAP_PROP_FPS) # 1倍速
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out10 = cv2.VideoWriter(iphone_temp, fourcc, fps10, (w_p_out, h_p_out))

while True:
    ret, frame = cap10.read()
    if not ret: break
    # iPhone 画面全域 (x=486, y=7, w=308, h=708)
    crop = frame[7:7+708, 486:486+308]
    resized = cv2.resize(crop, (w_phone, h_phone), interpolation=cv2.INTER_LANCZOS4)
    canvas = np.zeros((h_p_out, w_p_out, 3), dtype=np.uint8)
    canvas[y_phone_off:y_phone_off+h_phone, x_phone_off:x_phone_off+w_phone] = resized
    final_f = (canvas * mask_phone_3ch).astype(np.uint8)
    out10.write(final_f)

cap10.release()
out10.release()

# avconvert で Safari 互換書き出し (1倍速)
subprocess.run(['avconvert', '--source', iphone_temp, '--preset', 'PresetHighestQuality', '--output', iphone_out, '--replace'], capture_output=True)
if os.path.exists(iphone_temp): os.remove(iphone_temp)
print(f"1.2x Ultra HD iPhone video generated: {iphone_out}")


# --- 2. Apple Watch 動画 ---
watch_in = os.path.join(src_dir, 'マイムービー 12.mp4')
watch_temp = os.path.join(dst_dir, 'temp_watch.mp4')
watch_out = os.path.join(dst_dir, 'metronomeandjam-watch.mp4')

w_w_out, h_w_out = 422, 514
mask_watch = np.zeros((h_w_out, w_w_out), dtype=np.uint8)
r_w = 55
x1_w, y1_w, x2_w, y2_w = 56, 44, 412, 510

cv2.rectangle(mask_watch, (x1_w+r_w, y1_w), (x2_w-r_w, y2_w), 255, -1)
cv2.rectangle(mask_watch, (x1_w, y1_w+r_w), (x2_w, y2_w-r_w), 255, -1)
cv2.circle(mask_watch, (x1_w+r_w, y1_w+r_w), r_w, 255, -1)
cv2.circle(mask_watch, (x2_w-r_w, y1_w+r_w), r_w, 255, -1)
cv2.circle(mask_watch, (x1_w+r_w, y2_w-r_w), r_w, 255, -1)
cv2.circle(mask_watch, (x2_w-r_w, y2_w-r_w), r_w, 255, -1)
mask_watch_3ch = cv2.cvtColor(mask_watch, cv2.COLOR_GRAY2BGR) / 255.0

cap12 = cv2.VideoCapture(watch_in)
fps12 = cap12.get(cv2.CAP_PROP_FPS) # 1倍速
out12 = cv2.VideoWriter(watch_temp, fourcc, fps12, (w_w_out, h_w_out))

while True:
    ret, frame = cap12.read()
    if not ret: break
    crop = frame[370:370+275, 535:535+210]
    resized = cv2.resize(crop, (356, 466), interpolation=cv2.INTER_LANCZOS4)
    canvas = np.zeros((h_w_out, w_w_out, 3), dtype=np.uint8)
    canvas[44:44+466, 56:56+356] = resized
    final_f = (canvas * mask_watch_3ch).astype(np.uint8)
    out12.write(final_f)

cap12.release()
out12.release()

subprocess.run(['avconvert', '--source', watch_temp, '--preset', 'PresetHighestQuality', '--output', watch_out, '--replace'], capture_output=True)
if os.path.exists(watch_temp): os.remove(watch_temp)
print(f"Watch video generated: {watch_out}")
