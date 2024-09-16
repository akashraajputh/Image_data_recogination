import concurrent.futures
import pandas as pd
from pathlib import Path
from tqdm import tqdm

def download_image(image_link):
    filename = Path(image_link).name
    image_save_path = os.path.join(save_folder, filename)
    if not os.path.exists(image_save_path):
        try:
            urllib.request.urlretrieve(image_link, image_save_path)
        except Exception as e:
            print(f"Error downloading {image_link}: {e}")

df = pd.read_csv(r"/train.csv")

save_folder = r'/content/images'
os.makedirs(save_folder, exist_ok=True)

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    list(tqdm(executor.map(download_image, df['image_link']), total=len(df), desc="Downloading images"))
