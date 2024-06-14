import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages("sample.pdf"): 
#     for element in page_layout:
#         print(element )

text=extract_text("sample.pdf")
# print(text)

pattern=re.compile(r"[a-zA-Z]+,{1}\s{1}") #we are trying to gather words starting and ending with lowercase or uppercase followed by a comma(,) and a space
matches=pattern.findall(text)
# print(matches)
refined= [n[:-2] for n in matches] #we can use this to remove the comma(,) and space in the above 'matches' list.
print(refined)