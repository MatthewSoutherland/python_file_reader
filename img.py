with open("drill-sizes.jpg", "rb") as rf:
    with open("copy.txt", "w") as wf:
        chunk_size = 4000
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
