import streamlit as st
import torch
from PIL import Image
import numpy as np

def load_model(model_path):
    """Load the trained PyTorch model."""
    model = torch.load(model_path, map_location=torch.device('cpu'))
    model.eval()
    return model

def preprocess_image(image):
    """Preprocess the image for the model input."""
    image = image.resize((224, 224))  # Resize to model input size
    image = np.array(image).astype(np.float32) / 255.0  # Normalize
    image = np.transpose(image, (2, 0, 1))  # Change to (C, H, W)
    image = torch.tensor(image).unsqueeze(0)  # Add batch dimension
    return image

def predict(image, model):
    """Run the model on the image and return the predicted class."""
    with torch.no_grad():
        output = model(image)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        class_idx = torch.argmax(probabilities).item()
    return class_idx, probabilities[class_idx].item()

# Load the model
MODEL_PATH = '/mnt/data/best.pt'
model = load_model(MODEL_PATH)

# Streamlit app
st.title("Brain Tumor Detection App")

st.sidebar.title("Navigation")
menu = ["Home", "Upload Image"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.write("Welcome to the Brain Tumor Detection App.")
    st.write("This app uses a machine learning model to detect brain tumors from MRI images.")
    st.write("Navigate to the 'Upload Image' tab to get started.")

elif choice == "Upload Image":
    st.write("Upload an MRI image to detect brain tumor.")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        st.write("Processing image...")

        # Preprocess the image
        input_tensor = preprocess_image(image)

        # Get prediction
        class_idx, probability = predict(input_tensor, model)

        # Map class index to tumor type
        class_names = {
            0: "Axial Tumor",
            1: "Coronal Tumor",
            2: "Sagittal Tumor",
            3: "No Tumor"
        }

        prediction = class_names.get(class_idx, "Unknown")
        st.write(f"Prediction: {prediction}")
        st.write(f"Confidence: {probability:.2f}")
