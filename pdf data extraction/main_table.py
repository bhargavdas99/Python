import tabula

tables=tabula.read_pdf("table_sample.pdf",pages="all")
# print(tables[0])
df=tables[0]
print(df[df.Age>30])