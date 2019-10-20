import argparse

import numpy as np
import torch
from PIL import Image
from torchvision.transforms import ToTensor


parser = argparse.ArgumentParser(description='Super Resolution')
parser.add_argument('--model_pth', type=str, required=True, help='model .pth file, required')
parser.add_argument('--input_image', type=str, required=True, help='input image filename, required')
parser.add_argument('--output_image', type=str, default='out.jpg', help='image output file name (default: out.jpeg)')
parser.add_argument('--upscale_factor', type=int, default=2, help='super resolution upscale factor (default: 2)')
args = parser.parse_args()

img = Image.open(args.input_image).convert('YCbCr')
y, cb, cr = img.split()

net = torch.load(args.model_pth, map_location=torch.device('cpu'))
img_to_tensor = ToTensor()
input = img_to_tensor(y).view(1, -1, y.size[1], y.size[0])

out = net(input)
out_img_y = out[0].detach().numpy()
out_img_y *= 255.0
out_img_y = out_img_y.clip(0, 255)
out_img_y = Image.fromarray(np.uint8(out_img_y[0]), mode='L')

out_img_cb = cb.resize(out_img_y.size, Image.BICUBIC)
out_img_cr = cr.resize(out_img_y.size, Image.BICUBIC)
out_img = Image.merge('YCbCr', [out_img_y, out_img_cb, out_img_cr]).convert('RGB')

out_img.save(args.output_image)
print('output image saved to ', args.output_image)
