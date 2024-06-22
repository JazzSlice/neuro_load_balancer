import torch.nn as nn
# LSTM для предиктивной балансировки
class LSTMPredictiveModel(nn.Module):
    def __init__(self):
        super(LSTMPredictiveModel, self).__init__()
        self.lstm = nn.LSTM(input_size=10, hidden_size=128, num_layers=2)
        self.fc = nn.Linear(128, 1)
    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])
# CNN для интеллектуальной маршрутизации
class CNNRoutingModel(nn.Module):
    def __init__(self):
        super(CNNRoutingModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 64, kernel_size=3)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3)
        # Другие сверточные и полносвязные слои
        self.fc1 = nn.Linear(128 * 5 * 5, 1024)
        self.fc2 = nn.Linear(1024, 80)
    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        # Другие сверточные и pooling слои
        out = out.view(out.size(0), -1)
        out = self.fc1(out)
        return self.fc2(out)
# MLP для адаптивной балансировки
class MLPAdaptiveModel(nn.Module):
    def __init__(self):
        super(MLPAdaptiveModel, self).__init__()
        self.fc1 = nn.Linear(5, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 32)
        self.fc4 = nn.Linear(32, 1)
    def forward(self, x):
        out = self.fc1(x)
        out = self.fc2(out)
        out = self.fc3(out)
        return self.fc4(out)
