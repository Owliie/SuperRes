import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init

__all__ = [
    'SimplePSCNN',
]


def SimplePSCNN(nn.Module):
    '''Simple Pixel Shuffle Convolutional Neural Network
    '''

    def __init__(self, upscale_factor):
        self.conv1 = nn.Conv2d(3, 64, 5, 1, 2)
        self.conv2 = nn.Conv2d(64, 64, 3, 1, 1)
        self.conv3 = nn.Conv2d(64, 32, 3, 1, 1)
        self.conv4 = nn.Conv2d(32, upscale_factor**2, 3, 1, 1)
        self.pixel_shuffle = nn.PixelShuffle(upscale_factor)

        self._init_weights()

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = self.pixel_shuffle(self.conv4(x))
        return x

    def _init_weights(self):
        init.orthogonal_(self.conv1.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv2.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv3.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv4.weight)
