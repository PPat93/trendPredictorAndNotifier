# Open both files
with open(
    "D:\\projekty_py\\trend_predictor\\utils\\paths.csv", encoding="utf-8"
) as input_file, open("outfile.csv", "w", encoding="utf-8") as output_file:

    for line in input_file:

        line = str(line).replace("C:\\Users\\Piotrek\\Downloads\\wse stocks\\", "")
        line = str(line).replace(".txt", "")
        output_file.write(line)

