from sys import path_hooks

from PIL import Image, ImageDraw, ImageFont

print("Meme Generator Launched!")

top_text = input("Enter top text: ")
bottom_text = input("Enter bottom text: ")

print(top_text, bottom_text)

print('List of Images:')
print("1. Cat in restaurant")
print("2. Cat in glasses")
print("3. Surprised cat")
print("4. Pew, pew, pew")

chose_picture = input("Enter the number of your choice: ")

if chose_picture == "1":
    print("You chose: cat in restaurant")
    path_to_picture = "cat_in_restaurant.png"
elif chose_picture == "2":
    print("You chose: cat in glasses")
    path_to_picture = "cat_in_glasses.png"
elif chose_picture == "3":
    print("You chose: surprised cat")
    path_to_picture = "suprised_cat.png"
elif chose_picture == "4":
    print("You chose: pew, pew, pew")
    path_to_picture = "pew_pew_pew.png"

image = Image.open(path_to_picture)

draw = ImageDraw.Draw(image)

path_to_font = "./Tiny5/Tiny5-Regular.ttf"
font = ImageFont.truetype(path_to_font, size = 40)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((1011 - text_width) / 2, 10), top_text, font = font, fill = "white")


text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((1011 - text_width) / 2, 1321 - text_height), bottom_text, font = font, fill = "white")

image.save("new_meme.png")
print("Image compiled successfully")