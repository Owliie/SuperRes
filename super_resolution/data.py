import tarfile
import urllib.request
from os import makedirs, remove
from os.path import basename, exists, join

__all__ = [
    'download_bsd300',
]


def download_bsd300(dest='./dataset'):
    output_image_dir = join(dest, 'BSDS300/images')
    url = 'http://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300-images.tgz'

    if not exists(dest) and not exists(output_image_dir):
        makedirs(dest)

        print('downloading url...', url)
        data = urllib.request.urlopen(url)

        file_path = join(dest, basename(url))
        with open(file_path, 'wb') as f:
            f.write(data.read())

        print('extracting data...')
        with tarfile.open(file_path) as tar:
            for item in tar:
                tar.extract(item, dest)

        remove(file_path)

    return output_image_dir


if __name__ == '__main__':
    print('Dataset downloaded to', download_bsd300())
