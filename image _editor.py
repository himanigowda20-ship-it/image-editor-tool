from google.colab import files
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# Upload image
uploaded = files.upload()
filename = list(uploaded.keys())[0]
img = Image.open(filename).convert("RGB")

edited_image = img.copy()

def update(brightness, contrast, exposure, saturation):
    global edited_image

    edited_image = img.copy()

    # Adjustments
    edited_image = ImageEnhance.Brightness(edited_image).enhance(brightness)
    edited_image = ImageEnhance.Contrast(edited_image).enhance(contrast)
    edited_image = ImageEnhance.Brightness(edited_image).enhance(exposure)
    edited_image = ImageEnhance.Color(edited_image).enhance(saturation)

    plt.figure(figsize=(8,8))
    plt.imshow(edited_image)
    plt.axis("off")
    plt.show()

widgets.interact(
    update,
    brightness=(0.1, 3.0, 0.1),
    contrast=(0.1, 3.0, 0.1),
    exposure=(0.1, 3.0, 0.1),
    saturation=(0.0, 3.0, 0.1)
)

# Save button
def save_image(b):
    edited_image.save("edited_image.jpg")
    files.download("edited_image.jpg")

save_btn = widgets.Button(description="Save & Download")
save_btn.on_click(save_image)

display(save_btn)
