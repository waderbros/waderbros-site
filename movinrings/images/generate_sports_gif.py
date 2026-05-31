
from PIL import Image
import os

# 画像のディレクトリとファイル名リスト
dir_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/'
image_files = [f'Sports-{i}.png' for i in range(1, 11)]

# 画像を読み込み
images = []
for filename in image_files:
    img = Image.open(os.path.join(dir_path, filename))
    images.append(img)

# GIFを保存
output_path = os.path.join(dir_path, 'sports-animation.gif')
images[0].save(
    output_path,
    save_all=True,
    append_images=images[1:],
    duration=1000,  # 1フレームあたり1000ms
    loop=0         # ループ回数 (0は無制限)
)
print(f"GIF saved to {output_path}")
