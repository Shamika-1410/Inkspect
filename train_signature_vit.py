import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split
import timm
import os

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("CUDA " , torch.cuda.is_available())
# Define transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize images to 224x224 for ViT
    transforms.ToTensor(),           # Convert images to tensors
    transforms.Normalize([0.5], [0.5])  # Normalize for better training
])

# Load dataset
data_dir = "./dataset"  # Update with your dataset path
dataset = datasets.ImageFolder(root=data_dir, transform=transform)

# Split into train and validation sets
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset, [train_size, val_size])

# Create data loaders
batch_size = 32
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# Class names
class_names = dataset.classes
print(f"Classes: {class_names}")

# Define Vision Transformer model
class SignatureForgeryModel(nn.Module):
    def __init__(self, num_classes=2):  # Corrected
        super(SignatureForgeryModel, self).__init__()  # Corrected
        self.model = timm.create_model('vit_base_patch16_224', pretrained=True)
        self.model.head = nn.Linear(self.model.head.in_features, num_classes)

    def forward(self, x):
        return self.model(x)

# Initialize model
model = SignatureForgeryModel().to(device)

# Define loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=0.0001)

# Training function with progress tracking and model saving
def train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs=5):
    model.train()
    for epoch in range(num_epochs):
        train_loss, correct, total = 0, 0, 0
        batch_count = len(train_loader)

        for batch_idx, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

            # Progress tracking
            progress = (batch_idx + 1) / batch_count * 100
            print(f"Epoch [{epoch + 1}/{num_epochs}], Batch [{batch_idx + 1}/{batch_count}], Completion: {progress:.2f}%")

        train_acc = 100 * correct / total
        print(f"Epoch [{epoch + 1}/{num_epochs}] Completed, Loss: {train_loss:.4f}, Accuracy: {train_acc:.2f}%")

        # Save model after each epoch
        torch.save(model.state_dict(), f"signature_forgery_vit_epoch_{epoch + 1}.pth")
        print(f"Model saved for epoch {epoch + 1}")

# Train the model
train_model(model, train_loader, val_loader, criterion, optimizer, num_epochs=5)

# Evaluation function
def evaluate_model(model, val_loader):
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f"Validation Accuracy: {accuracy:.2f}%")

# Evaluate the model
evaluate_model(model, val_loader)