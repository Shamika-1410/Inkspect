import torch
import torch.nn as nn
import torchvision.transforms as transforms
import timm
from PIL import Image
import os
import re

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("CUDA", torch.cuda.is_available())

# Define transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

# Define model
class SignatureForgeryModel(nn.Module):
    def __init__(self, num_classes=2):
        super(SignatureForgeryModel, self).__init__()
        self.model = timm.create_model('vit_base_patch16_224', pretrained=True)
        self.model.head = nn.Linear(self.model.head.in_features, num_classes)

    def forward(self, x):
        return self.model(x)

# Load model
model = SignatureForgeryModel().to(device)
model_dir = "."
model_files = [f for f in os.listdir(model_dir) if re.match(r"signature_forgery_vit_epoch_\d+.pth", f)]
last_epoch = max([int(re.search(r"\d+", f).group()) for f in model_files], default=0)

if last_epoch > 0:
    model.load_state_dict(torch.load(f"signature_forgery_vit_epoch_{last_epoch}.pth"))
    model.eval()
    print(f"Model loaded from epoch {last_epoch}")
else:
    print("No trained model found.")
    exit()

# Prediction function
def predict(image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        return "Genuine" if predicted.item() == 1 else "Forged"

# Test model
test_image_path = "./test_ruled.jpg"
result = predict(test_image_path)
print(f"Prediction: {result}")
