import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from ultralytics import YOLO

# Path model upload
uploaded_model = 'best.pt'

# Load YOLO model
model = YOLO(uploaded_model)

st.title("Brain Tumor Detection App")
st.write("Upload images to detect brain tumors using the YOLO model.")

# File uploader for image input
uploaded_files = st.file_uploader("Choose images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    st.write("### Uploaded Images")
    
    # Container for displaying uploaded images
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=uploaded_file.name, use_column_width=True)

    if st.button("Detect Tumors"):
        st.write("### Detection Results")
        
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            
            # Perform prediction
            results = model.predict(source=image, conf=0.25)
            
            # Display results
            fig, ax = plt.subplots()
            ax.imshow(results[0].plot())  # Display image with bounding box
            ax.axis("off")
            st.pyplot(fig)
