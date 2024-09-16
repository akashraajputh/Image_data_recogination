import requests
import os

def download_images(df, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for index, row in df.iterrows():
        #here we need to paste the link of the image
        image_url = row['image_link']
        image_name = f"{output_dir}/{index}.jpg"
        try:
            img_data = requests.get(image_url).content
            with open(image_name, 'wb') as handler:
                handler.write(img_data)
        except Exception as e:
            print(f"Error downloading {image_url}: {e}")

# Assuming 'df' is the DataFrame with image URLs
# download_images(df, 'images/')
