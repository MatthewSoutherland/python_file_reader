import tabula

pdf_path = "sample.pdf"

# args: path, created file name, file type, page to inspect
tabula.convert_into(pdf_path, "first_csv_table", output_format="csv", pages="1")
