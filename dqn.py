import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import namedtuple
import random

class DQN(nn.Module):
    def __init__(self, h, w, outputs):
        super(DQN, self).__init__()

        self.conv1 = nn.Conv2d(4, 16, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        
        self.relu = nn.ReLU()

        self.fc1 = nn.Linear(28224, 512)
        self.fc2 = nn.Linear(28224, 2)
        self.fc3 = nn.Linear(28224, 128)


        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.Linear):
                nn.init.uniform_(m.weight, -0.01, 0.01)
                nn.init.constant_(m.bias, 0)
                

    def forward(self, x):

        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.relu(self.conv2(x))

        x = x.view(x.size(0), -1)

        x = self.fc3(x)

        return x



