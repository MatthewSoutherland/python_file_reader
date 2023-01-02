import tabula


# pip install tabula-py
import tabula

pdf_path = "rfpt.pdf"
tabula.convert_into(pdf_path, "rosenport.csv", output_format="csv", pages="1")
