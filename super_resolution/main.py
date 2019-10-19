import argparse
from math import log10
from os.path import join

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader

from data import get_test_set, get_train_set
from models import PixelShuffleCNN


# Train Settings
parser = argparse.ArgumentParser(description='Super Resolution Training')
parser.add_argument('--upscale_factor', type=int, default=4, help='super resolution upscale factor (default: 4)')
parser.add_argument('--batch_size', type=int, default=64, help='training batch size (default: 64)')
parser.add_argument('--test_batch_size', type=int, default=10, help='testing batch size (default: 10)')
parser.add_argument('--epochs', type=int, default=2, help='number of epochs to train for (default: 2)')
parser.add_argument('--lr', type=float, default=0.01, help='learnig rate (default: 0.01)')
parser.add_argument('--cuda', action='store_true', help='use cuda?')
parser.add_argument('--threads', type=int, default=0, help='number of threads for data loader to use (default: 0)')
parser.add_argument('--pth_dir', type=str, default='checkpoints', help='where to save model checkpoints (default: checkpoints)')
args = parser.parse_args()

print(args, end='\n\n')

# Load Train/Test set
## Train
print('Load Train set')
print('='*15)
train_set = get_train_set(upscale_factor=args.upscale_factor)
train_set_loader = DataLoader(dataset=train_set, batch_size=args.batch_size, num_workers=args.threads, shuffle=True)

## Test
print('Load Test set')
print('='*15)
test_set = get_test_set(upscale_factor=args.upscale_factor)
test_set_loader = DataLoader(dataset=test_set, batch_size=args.test_batch_size, num_workers=args.threads, shuffle=True)

# Init Model
print('Building the model')
print('='*30)
net = PixelShuffleCNN(args.upscale_factor)

## Criterion
criterion = nn.MSELoss()
## Optimizer
optimizer = optim.Adam(net.parameters(), lr=args.lr)


# Train step
def train(epoch):
    epoch_loss = 0.0

    for i, data in enumerate(train_set_loader):
        input, target = data

        optimizer.zero_grad()

        output = net(input)
        loss = criterion(output, target)
        epoch_loss += loss.item()

        loss.backward()
        optimizer.step()

        print(f'===> Epoch[{epoch}]({i}/{len(train_set_loader)}): Loss: {round(loss.item(), 4)}')

    print(f'=====> Epoch {epoch} Complete: Avg. Loss: {round(epoch_loss / len(train_set_loader), 4)}')

# Test step
def test():
    avg_psnr = 0
    with torch.no_grad():
        for data in test_set_loader:
            input, target = data

            output = net(input)
            mse = criterion(output, target)
            psnr = 10 * log10(1 / mse.item())
            avg_psnr += psnr

    print(f'=======> Avg. PSNR: {round(avg_psnr / len(test_set_loader), 4)} dB')

# Checkpoint step
def checkpoint(epoch):
    path = join(args.out, f'model-epoch-{epoch}.pth')
    torch.save(net.state_dict(), path)
    print(f'Checkpoint saved to {path}')

# RUN
print()
for epoch in range(1, args.epochs+1):
    train(epoch)
    test()
    checkpoint(epoch)
    print()
