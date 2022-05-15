# Create random-color images with Python


How to paint different colors on canvas with Python? First of all, let's 

#### import two modules


```python
import random
from PIL import Image 
```

We use module `ramdon` as a digit creator.

`PIL` is the de facto image process standard module in Python.

#### Create a single picture with a random color

```python
i = 0
```
This step will facilitate you to write the next iteration step.

You can easily change the 'i=0' line to 'for i in range(10):'  and indent the following codes

Then, Set the RGB single color randomly

```python
color1 = random.randint(0,255)
color2 = random.randint(0,255)
color3 = random.randint(0,255)
background_color = (color1, color2, color3)
```
Create a canvas with a specific color and a scale with 680 long × 200 width
```python
img_obj = Image.new('RGB', (680, 200), background_color)
```
Save the image
```python
with open("title_en_pic_{0:03d}.png".format(i+1), "wb") as f:
    img_obj.save(f, "png")
```
`{0:03d}` means use `0` to fill the number until `1` turn to three digits `001`

We can see a random-color image in your default path: title_en_pic_001.png

![](https://doraemonj.github.io/pics/title_en_pic_001.png)

#### Make 10 random-color images with an additional code:

Just change the line `i = 0`, and indent all the following lines:

```python
# Change the below first line only:
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
```

Ten pictures emerge in one second:

![screenshot_20220515_203550](https://doraemonj.github.io/pics/screenshot_20220515_203550.png)

#### Attachments

​	[Source code download: title_image.py](https://doraemonj.github.io/docs/title_image.py)


