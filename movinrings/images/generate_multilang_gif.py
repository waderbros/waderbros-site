from PIL import Image
import os

dir_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/'
image_files = [f'Languages-{i}.png' for i in range(1, 10)]

images = []
for filename in image_files:
    img = Image.open(os.path.join(dir_path, filename))
    images.append(img)

output_path = os.path.join(dir_path, 'multi-language.gif')
images[0].save(
    output_path,
    save_all=True,
    append_images=images[1:],
    duration=1600,  # 既存設定と同じ1.6秒
    loop=0         # ループ無制限
)
print(f"GIF saved to {output_path}")
