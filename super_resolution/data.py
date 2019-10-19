import tarfile
import urllib.request
from os import makedirs, remove
from os.path import basename, exists, join

from torchvision.transforms import transforms

from CONFIG import *
from dataset import DatasetFromFolder

__all__ = [
    'download_bsd300',
    'input_transform',
    'target_transform',
    'get_train_set',
    'get_test_set',
]


def download_bsd300(dest='./dataset'):
    output_image_dir = join(dest, 'BSDS300/images')
    url = 'http://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300-images.tgz'

    if not exists(dest) and not exists(output_image_dir):
        makedirs(dest)

        print('downloading url...', url)
        data = urllib.request.urlopen(url)

        filepath = join(dest, basename(url))
        with open(filepath, 'wb') as f:
            f.write(data.read())

        print('extracting data...')
        with tarfile.open(filepath) as tar:
            for item in tar:
                tar.extract(item, dest)

        remove(filepath)

    return output_image_dir

def calculate_valid_size(size, scale_factor):
    return size - (size % scale_factor)

def input_transform(h, w, scale_factor):
    return transforms.Compose([
        transforms.CenterCrop((h, w)),
        transforms.Resize((h // scale_factor, w // scale_factor)),
        transforms.ToTensor(),
    ])

def target_transform(h, w):
    return transforms.Compose([
        transforms.CenterCrop((h, w)),
        transforms.ToTensor(),
    ])

def get_train_set(h=IMAGE_HEIGHT, w=IMAGE_WIDTH, scale_factor=SCALE_FACTOR):
    h = calculate_valid_size(h, scale_factor)
    w = calculate_valid_size(w, scale_factor)

    return DatasetFromFolder(
        join(download_bsd300(), 'train'),
        input_transfrom=input_transform(h, w, scale_factor),
        target_transform=target_transform(h, w),
    )

def get_test_set(h=IMAGE_HEIGHT, w=IMAGE_WIDTH, scale_factor=SCALE_FACTOR):
    h = calculate_valid_size(h, scale_factor)
    w = calculate_valid_size(w, scale_factor)

    return DatasetFromFolder(
        join(download_bsd300(), 'test'),
        input_transfrom=input_transform(h, w, scale_factor),
        target_transform=target_transform(h, w),
    )



if __name__ == '__main__':
    print('Dataset downloaded to', download_bsd300())
