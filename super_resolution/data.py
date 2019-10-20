import tarfile
import urllib.request
import zipfile
from os import makedirs, remove
from os.path import basename, exists, join

import requests
from torchvision.transforms import transforms

from CONFIG import *
from dataset import DatasetFromFolder


__all__ = [
    'download_bsd300',
    'download_file_from_google_drive',
    'get_confirm_token',
    'save_response_content',
    'download_nasa_apod',
    'calculate_valid_size',
    'input_transform',
    'target_transform',
    'get_train_set',
    'get_test_set',
]


def download_bsd300(dest='./dataset'):
    output_image_dir = join(dest, 'BSDS300/images')
    url = 'http://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300-images.tgz'

    if not exists(dest):
        makedirs(dest)

    if not exists(output_image_dir):

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

def download_file_from_google_drive(id, destination):
    url = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(url, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(url, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    chunk_size = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(chunk_size):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def download_nasa_apod(dest='./dataset'):
    output_image_dir = join(dest, 'NASA/images')
    file_id = '19a36iKIcQZRgYWyQXN7UGf3dbBx8VI9E'

    if not exists(dest):
        makedirs(dest)

    if not exists(output_image_dir):
        filepath = join(dest, 'images.zip')

        print('downloading file from google drive...', file_id)        
        download_file_from_google_drive(file_id, filepath)

        print('extracting data...')
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(join(dest, 'NASA/'))

        remove(filepath)

    return output_image_dir

def calculate_valid_size(size, upscale_factor):
    return size - (size % upscale_factor)

def input_transform(h, w, upscale_factor):
    return transforms.Compose([
        transforms.CenterCrop((h, w)),
        transforms.Resize((h // upscale_factor, w // upscale_factor)),
        transforms.ToTensor(),
    ])

def target_transform(h, w):
    return transforms.Compose([
        transforms.CenterCrop((h, w)),
        transforms.ToTensor(),
    ])

def get_train_set(h=IMAGE_HEIGHT, w=IMAGE_WIDTH, download=download_bsd300, upscale_factor=None):
    h = calculate_valid_size(h, upscale_factor)
    w = calculate_valid_size(w, upscale_factor)

    return DatasetFromFolder(
        join(download(), 'train'),
        input_transfrom=input_transform(h, w, upscale_factor),
        target_transform=target_transform(h, w),
    )

def get_test_set(h=IMAGE_HEIGHT, w=IMAGE_WIDTH, download=download_bsd300, upscale_factor=None):
    h = calculate_valid_size(h, upscale_factor)
    w = calculate_valid_size(w, upscale_factor)

    return DatasetFromFolder(
        join(download(), 'test'),
        input_transfrom=input_transform(h, w, upscale_factor),
        target_transform=target_transform(h, w),
    )



if __name__ == '__main__':
    print('BSD300 Dataset downloaded to', download_bsd300())
    print('NASA APOD Dataset downloaded to', download_nasa_apod())
