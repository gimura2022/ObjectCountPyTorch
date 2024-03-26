from PIL import Image, ImageDraw
import random
import tqdm
import pandas

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

data = {
    "file_name": [],
    "count": []
}

for i in tqdm.tqdm(range(5000)):
    image = Image.new("RGBA", (28, 28), get_random_color())
    image_drawer = ImageDraw.Draw(image)

    count = random.randint(1, 7)

    data["count"].append(count)
    data["file_name"].append(f"img_{i}.png")

    for j in range(count):
        x = random.randint(0, 28)
        y = random.randint(0, 28)
        width = random.randint(2, 8)
        height = random.randint(2, 8)

        image_drawer.rectangle((x, y, width + x, height + y), fill=get_random_color(), outline=get_random_color())

    image = image.convert("L")

    image.save(f"C:\\Users\\glebm\\OneDrive\\Рабочий стол\\Projects\\Half_2_Engine\\ObjectCountPyTorch\\data\\train\\images\\normal\\img_{i}.png")

pandas.DataFrame(data).to_csv("C:\\Users\\glebm\\OneDrive\\Рабочий стол\\Projects\\Half_2_Engine\\ObjectCountPyTorch\\data\\train\\images.csv")