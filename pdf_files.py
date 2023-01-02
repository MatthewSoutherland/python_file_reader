import re
from pdfminer.high_level import extract_text

text = extract_text("rfpt.pdf")
print(text)

# for pageLayout in extract_pages("rfpt.pdf"):
#     for element in pageLayout:
#         print(element)
