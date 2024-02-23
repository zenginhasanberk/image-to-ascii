import sys
from PIL import Image
import numpy as np

def main():
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Incorrect usage. Example: python3 image_to_ascii {input_filename} {height} {optional:output_filename}")
        exit(-1)

    try:
        height = int(sys.argv[2])
    except:
        print("You provided a non-integer height!")
        print("Incorrect usage. Example: python3 image_to_ascii {input_filename} {height} {optional:output_filename}")
        exit(-1)

    img = load_image(sys.argv[1])
    img = resize_img(img, height) 
    art = image_to_ascii(img)

    if len(sys.argv) == 3:
        print(art)
    elif len(sys.argv) == 4:
        with open(sys.argv[3], 'w') as file:
            file.write(art)

    return 0

def load_image(input_filename: str) -> Image.Image:
    return Image.open(input_filename).convert('L')

def resize_img(image: Image.Image, new_height: int) -> Image.Image:
   old_width, old_height = image.size
   ratio = old_width / old_height
   new_width = int(ratio * new_height)
   return image.resize((new_width, new_height))

def image_to_ascii(image: Image.Image, chars="@%#*+=-:. ") -> str:
    image_arr = np.array(image)
    normalized_arr = np.interp(image_arr, (image_arr.min(), image_arr.max()), (0, len(chars)-1))
    art = np.vectorize(lambda x: chars[int(x)])(normalized_arr)
    return "{}".format("\n".join("".join(row) for row in art))

if __name__ == "__main__":
    main()
