import tabula

pdf_path = "sample.pdf"

dfs = tabula.read_pdf(pdf_path, pages="2")
for i in range(len(dfs)):
    dfs[i].to_csv(f"page_two_table{i}.csv")
