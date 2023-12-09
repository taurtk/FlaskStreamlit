from flask import app
import streamlit as st
from PIL import Image, ImageDraw
from flask_cors import CORS

# CORS(app)

def main():
    st.title("Object Removal App")

    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        
        label_objects(image)

def label_objects(image):
    st.subheader("Object Labeling")

    # Get user input for labeling objects
    num_objects = st.number_input("Enter the number of objects:", min_value=1, max_value=10, value=1, step=1)

    # Initialize a list to store object labels
    object_labels = []

    # Checkbox for each object
    for i in range(1, num_objects + 1):
        label = st.checkbox(f"Object {i}", key=f"object_{i}")
        if label:
            object_labels.append(i)

    # Button to apply object labeling
    if st.button("Apply Object Labeling"):
        # Process the image and draw labels
        labeled_image = draw_labels(image, object_labels)
        st.image(labeled_image, caption="Labeled Image.", use_column_width=True)

def draw_labels(image, object_labels):
    # Create a copy of the image to draw on
    labeled_image = image.copy()
    draw = ImageDraw.Draw(labeled_image)

    # Draw labels on the image
    for label in object_labels:
        draw.text((10, 10 * label), f"Object {label}", fill="red")

    return labeled_image

if __name__ == "__main__":
    main()
