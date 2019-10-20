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
img = Image.open(args.input_image).convert('YCbCr')

Y, Cb, Cr = img.split()
input = ToTensor()(Y).view(1, -1, Y.size[1], Y.size[0])
output = net(input)[0].detach().numpy()

def YtoRGB(x):
    x *= 255
    x = x.clip(0, 255)

    out_img_Y = Image.fromarray(np.uint8(x[0]), mode='L')
    out_img_Cb = Cb.resize(out_img_Y.size, Image.BICUBIC)
    out_img_Cr = Cr.resize(out_img_Y.size, Image.BICUBIC)
    out_img = Image.merge('YCbCr', [out_img_Y, out_img_Cb, out_img_Cr]).convert('RGB')

    return out_img

out_img = YtoRGB(output)
out_img.save(args.output_image)
print('output image saved to ', args.output_image)
