import pandas as pd
from pathlib import Path
import pytesseract
from PIL import Image
import os
from tqdm import tqdm  # Import tqdm for the progress bar

# Function to extract text from an image
def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from {image_path}: {e}")
        return ""

# Function to extract text features from images and show progress
def extract_text_features(df, image_folder):
    texts = []
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Extracting text from images"):
        image_path = os.path.join(image_folder, Path(row['image_link']).name)
        text = extract_text_from_image(image_path)
        texts.append(text)
    return texts

# Load your DataFrame and set the image folder
df = pd.read_csv('/train.csv')
image_folder = '/content/images'

# Extract text features and add progress bar
texts = extract_text_features(df, image_folder)

# Add extracted texts to the DataFrame
df['extracted_text'] = texts

# Display the DataFrame to check if texts have been added
print(df.head())
