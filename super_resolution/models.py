import torch.nn as nn
import torch.nn.functional as F
import torch.nn.init as init
import torchvision.models as models

__all__ = [
    'PixelShuffleCNN',
    'ResPixelShuffleCNN',
]


class PixelShuffleCNN(nn.Module):
    def __init__(self, upscale_factor):
        super(PixelShuffleCNN, self).__init__()
        self.upscale_factor = upscale_factor

        self.conv1 = nn.Conv2d(1, 64, 5, 1, 2)
        self.conv2 = nn.Conv2d(64, 64, 3, 1, 1)
        self.conv3 = nn.Conv2d(64, 32, 3, 1, 1)
        self.conv4 = nn.Conv2d(32, self.upscale_factor**2, 3, 1, 1)

        self._initialize_weights()

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = self.conv4(x)
        x = F.pixel_shuffle(x, self.upscale_factor)
        return x

    def _initialize_weights(self):
        init.orthogonal_(self.conv1.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv2.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv3.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv4.weight)

class ResPixelShuffleCNN(nn.Module):

    def __init__(self, upscale_factor):
        super(ResPixelShuffleCNN, self).__init__()
        self.upscale_factor = upscale_factor

        resnet = models.resnet34(pretrained=True)

        self.conv1 = nn.Conv2d(1, 64, 5, 1, 2)

        resnet.layer1.requires_grad_(False)
        self.resblock1 = resnet.layer1
        resnet.layer2.requires_grad_(False)
        self.resblock2 = resnet.layer2
        resnet.layer3.requires_grad_(False)
        self.resblock3 = resnet.layer3

        self.conv2 = nn.Conv2d(256, 256, 3, 1, 1)
        self.conv3 = nn.Conv2d(256, 128, 3, 1, 1)
        self.conv4 = nn.Conv2d(128, 64, 3, 1, 1)
        self.conv5 = nn.Conv2d(64, 32, 3, 1, 1)

        self.conv6 = nn.Conv2d(32, self.upscale_factor**2, 3, 1, 1)
        self.conv7 = nn.Conv2d(1, self.upscale_factor**2, 3, 1, 1)

        self._initialize_weights()

    def forward(self, x):
        x = F.relu(self.conv1(x))

        x = self.resblock1(x)
        x = self.resblock2(x)
        x = self.resblock3(x)

        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = F.relu(self.conv5(x))

        x = self.conv6(x)
        x = F.pixel_shuffle(x, self.upscale_factor)
        x = self.conv7(x)
        x = F.pixel_shuffle(x, self.upscale_factor)

        return x

    def _initialize_weights(self):
        init.orthogonal_(self.conv1.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv2.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv3.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv4.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv5.weight, init.calculate_gain('relu'))
        init.orthogonal_(self.conv6.weight)
        init.orthogonal_(self.conv7.weight)
