from math import sqrt
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
import torchvision.models as models

__all__ = [
    'PixelShuffleCNN',
    'GradualPixelShuffleCNN',
]


class PixelShuffleCNN(nn.Module):
    def __init__(self, upscale_factor):
        super(PixelShuffleCNN, self).__init__()
        self.upscale_factor = upscale_factor

        self.conv1 = nn.Conv2d(1, 64, 5, 1, 2)
        self.conv2 = nn.Conv2d(64, 128, 5, 1, 2)
        self.conv3 = nn.Conv2d(128, 256, 3, 1, 1)
        self.conv4 = nn.Conv2d(256, 128, 3, 1, 1)

        self.conv5 = nn.Conv2d(128, self.upscale_factor**2, 3, 1, 1)

        self._initialize_weights()

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))

        x = self.conv5(x)
        x = F.pixel_shuffle(x, self.upscale_factor)
        return x

    def _initialize_weights(self):
        init.orthogonal_(self.conv1.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv2.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv3.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv4.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv5.weight)

class GradualPixelShuffleCNN(nn.Module):
    def __init__(self, upscale_factor):
        if round(sqrt(upscale_factor)) != sqrt(upscale_factor):
            raise Exception('Upscale Factor must be a whole cube.')

        super(GradualPixelShuffleCNN, self).__init__()
        self.upscale_factor = upscale_factor

        self.conv1 = nn.Conv2d(1, 64, 5, 1, 2)
        self.conv2 = nn.Conv2d(64, 128, 5, 1, 2)
        self.conv3 = nn.Conv2d(128, 256, 3, 1, 1)
        self.conv4 = nn.Conv2d(256, 128, 3, 1, 1)

        self.conv5 = nn.Conv2d(128, self.upscale_factor, 3, 1, 1)

        self.conv6 = nn.Conv2d(1, 64, 5, 1, 2)
        self.conv7 = nn.Conv2d(64, 128, 5, 1, 2)

        self.conv8 = nn.Conv2d(128, self.upscale_factor, 3, 1, 1)

        self._initialize_weights()

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))

        x = self.conv5(x)
        x = F.pixel_shuffle(x, int(sqrt(self.upscale_factor)))

        x = F.relu(self.conv6(x))
        x = F.relu(self.conv7(x))

        x = self.conv8(x)
        x = F.pixel_shuffle(x, int(sqrt(self.upscale_factor)))

        return x

    def _initialize_weights(self):
        init.orthogonal_(self.conv1.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv2.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv3.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv4.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv5.weight)
        init.orthogonal_(self.conv6.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv7.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv8.weight)
