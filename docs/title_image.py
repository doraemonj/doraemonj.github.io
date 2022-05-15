# Use python to create image with random colors

# Before the task, let's import modules
import random                                   # ramdon digit creator
from PIL import Image                           # PIL is the de facto image process standard in Python
## 1. Create a single picture with a random color

# This step will facilitate you to write the next iteration step
# Tips: you can easily change the 'i=0' line to 'for i in range(10):'  and indent the following codes
for i in range(10):

    # Set the RGB single color randomly
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    background_color = (color1, color2, color3)

    # Create a canvas with a specific color and a scale with 680 long × 200 width
    img_obj = Image.new('RGB', (680, 200), background_color)

    # Save the image
    with open("title_en_pic_{0:03d}.png".format(i+1), "wb") as f:
        img_obj.save(f, "png")
