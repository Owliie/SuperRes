import argparse

from PIL import Image
from torchvision.transforms import ToPILImage

from CONFIG import *
from data import calculate_valid_size, input_transform


# Settings
parser = argparse.ArgumentParser(description='Down scale an input image')
parser.add_argument('--input_image', type=str, required=True, help='the input image')
parser.add_argument('--downscale_factor', type=int, required=True, help='resolution downscale factor, required')
parser.add_argument('--output_image', type=str, default='out.jpg', help='output image name (default: out.jpg)')
args = parser.parse_args()

# Set up
h, w = calculate_valid_size(IMAGE_HEIGHT, args.downscale_factor), \
        calculate_valid_size(IMAGE_WIDTH, args.downscale_factor)

transform = input_transform(h, w, args.downscale_factor)
to_pil = ToPILImage()

# Image
## Load
img = Image.open(args.input_image)
## Transform
img = transform(img)
img = to_pil(img)
## Save
img.save(args.output_image)

print('Output image saved to', args.output_image)
