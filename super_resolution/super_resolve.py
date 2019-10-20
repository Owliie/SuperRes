import argparse

import numpy as np
import torch
from PIL import Image
from torchvision.transforms import ToPILImage, ToTensor


# Settings
parser = argparse.ArgumentParser(description='Super Resolution')
parser.add_argument('--model_pth', type=str, required=True, help='model .pth file, required')
parser.add_argument('--input_image', type=str, required=True, help='input image filename, required')
parser.add_argument('--output_image', type=str, default='out.jpg', help='image output file name (default: out.jpeg)')
parser.add_argument('--upscale_factor', type=int, default=2, help='super resolution upscale factor (default: 2)')
args = parser.parse_args()

net = torch.load(args.model_pth, map_location=torch.device('cpu'))
img = Image.open(args.input_image).convert('RGB')
input = ToTensor()(img)

output = net(input)
out_img = ToPILImage(mode='RGB')(output)

out_img.save(args.output_image)
print('output image saved to ', args.output_image)
