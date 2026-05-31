
from PIL import Image

gif_path = '/Users/MasaWada2/Documents/GitHub/waderbros-site/movinrings/images/multi-language.gif'
img = Image.open(gif_path)

durations = []
try:
    while True:
        durations.append(img.info.get('duration', 0))
        img.seek(img.tell() + 1)
except EOFError:
    pass

print(f"Durations: {durations}")
