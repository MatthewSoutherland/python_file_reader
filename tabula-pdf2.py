import tabula

pdf_path = "sample.pdf"

dfs = tabula.read_pdf(pdf_path, pages="all")
for i in range(len(dfs)):
    dfs[i].to_csv(f"all_table{i}.csv")
