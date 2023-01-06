import pytesseract
from PIL import Image

# Open the image
image = Image.open("as1300.png")

# Extract the text
text = pytesseract.image_to_string(image)

# Print the text
print(text)
