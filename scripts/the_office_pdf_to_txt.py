# importing required modules
from PyPDF2 import PdfReader
import re

# global variables
mode = "append"  # append
pdf_file = "/home/samir/Documents/data/the_office/the-office-101-pilot-2005.pdf"
write_txt_file = "the_office/test_script.txt"
append_txt_file = "the_office/test_script.txt"

if mode == "write":
    txt_file = write_txt_file
elif mode == "append":
    txt_file = append_txt_file
else:
    print("choose mode write or append")
    exit()

##### Adding Sets of texts to look for in the screenplay
# Page numbers added to the delete set
delete_set = []
for i in range(100, 0, -1):
    number = str(i) + "\."
    delete_set.append(number)
print(delete_set)
# Add a line before these words/characters
new_line_before_set = {
    "SCOTT",
    "PAM",
    "JIM",
    "JAN",
    "DWIGHT",
    "OSCAR",
    "CREED",
    "ANGELA",
    "ANDY",
    "KEVIN",
    "STANLEY",
    "PHYLLIS",
    "HOLLY",
    "KELLY",
    "TOBY",
    "RYAN",
    "MEREDITH",
    "ROBERT",
    "GABE",
    "DARRYL",
    "ROY",
    "SCENE",
    "The End.",
}

# creating a pdf reader object
reader = PdfReader(pdf_file)

# find number of pages
num_pages = len(reader.pages)

# write to txt file
if mode == "write":
    open(txt_file, "w").write("")

# iterate through all the pages to edit
for i in range(num_pages):
    if i == 0:
        open(txt_file, "a").write("\n\nNEW SCREENPLAY:\n\n")
        continue
    # getting a specific page from the pdf file
    page = reader.pages[i]

    # extracting text from page
    text = page.extract_text()

    # delete page numbers
    for word in delete_set:
        for m in re.finditer(word, text):
            print(
                f"Page {i} found word {text[m.start():m.end()+1]} starting {m.start()} and ending {m.end()}"
            )
            text = text[: m.start()] + "\n\n" + text[m.end() + 2 :]

    # adding a line before certain word
    for word in new_line_before_set:
        add_i = 0
        for m in re.finditer(word, text):
            print(f"found word {word} starting {m.start()} and ending {m.end()}")
            text = text[: m.start() + add_i] + "\n" + text[m.start() + add_i :]
            add_i += 1

    open(txt_file, "a").write(text)
