
from PIL import Image
import os

def update_gif_duration(input_path, output_path, new_duration):
    img = Image.open(input_path)
    frames = []
    try:
        while True:
            frames.append(img.copy())
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=new_duration,
        loop=0
    )
    print(f"Updated {input_path} to {output_path} with duration {new_duration}ms")

dir_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/'
update_gif_duration(os.path.join(dir_path, 'sports-animation.gif'), os.path.join(dir_path, 'sports-animation.gif'), 1600)
update_gif_duration(os.path.join(dir_path, 'multi-language.gif'), os.path.join(dir_path, 'multi-language.gif'), 1600)
