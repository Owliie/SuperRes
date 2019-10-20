from os import listdir
from os.path import join

import torch.utils.data as data
from PIL import Image

__all__ = [
    'is_image_file',
    'load_image',
    'DatasetFromFolder',
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.gif'])

def load_image(filepath):
    img = Image.open(filepath).convert('RGB')
    return img

class DatasetFromFolder(data.Dataset):
    
    def __init__(self, folderpath, input_transfrom=None, target_transform=None):
        super(DatasetFromFolder, self).__init__()
        self.image_filenames = [join(folderpath, x) for x in listdir(folderpath) if is_image_file(x)]

        self.input_transfrom = input_transfrom
        self.target_transform = target_transform

    def __getitem__(self, idx):
        input = load_image(self.image_filenames[idx])
        target = input.copy()

        if self.input_transfrom:
            input = self.input_transfrom(input)
        if self.target_transform:
            target = self.target_transform(target)

        return input, target

    def __len__(self):
        return len(self.image_filenames)
