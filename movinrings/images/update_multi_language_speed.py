
from PIL import Image
import os

dir_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/'
input_gif = os.path.join(dir_path, 'multi-language.gif')
output_gif = os.path.join(dir_path, 'multi-language-1000ms.gif')

img = Image.open(input_gif)
frames = []
try:
    while True:
        frames.append(img.copy())
        img.seek(img.tell() + 1)
except EOFError:
    pass

frames[0].save(
    output_gif,
    save_all=True,
    append_images=frames[1:],
    duration=1000,
    loop=0
)
print(f"Saved to {output_gif}")
