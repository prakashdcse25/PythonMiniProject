from PIL import Image
import pytesseract

con="yes"

while con.lower() == "yes":
    name=input("Enter the name of the image :")
    try:
        img=Image.open(name+".png")
        text = pytesseract.image_to_string(img)
        print("\nThe Text in the image is :\n")
        print(text)
        print("All the contents in the image is printed sucssfully :) ")
    except FileNotFoundError:
        print(f"The image -'{name}' is not in the python folder location :( ")
        print("Try to move the image to the file location ...")
    print()

    con=input("Do you want to convert any other image(yes/no):")
    print()

print("The Program Executed Successfully...")

