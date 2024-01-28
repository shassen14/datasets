# importing required modules
from PyPDF2 import PdfReader
import re

# global variables
mode = "write"  # "write" or "append"
pdf_file = "/home/samir/Documents/data/the_office/1-TheOfficeSample-theMasseuse.pdf"
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
    number = str(i)  # + "\."
    delete_set.append(number)
# print(delete_set)
# Add a line before these words/characters
new_line_before_set = {
    "MICHAEL",
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
    "MARCI",
    "DONNA",
    "EMMA",
    "TODD",
    "FLASHBACK",
    "SCENE",
    "REVERSE ANGLE",
    "BACK TO PRESENT",
    "The End.",
    "THE END",
    "INT.",
    "END TEASER",
}

# creating a pdf reader object
reader = PdfReader(pdf_file)

# find number of pages
num_pages = len(reader.pages)
print(f"{num_pages} pages")

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
        line_add = ""
        n = len(line_add)
        for m in re.finditer(word, text):
            print(
                f"Page {i} found word {text[m.start():m.end()+n]} starting {m.start()} and ending {m.end()}"
            )
            text = text[: m.start()] + line_add + text[m.end() + n :]

    # adding a line before certain word
    for word in new_line_before_set:
        add_i = 0
        for m in re.finditer(word, text):
            print(f"found word {word} starting {m.start()} and ending {m.end()}")
            text = text[: m.start() + add_i] + "\n" + text[m.start() + add_i :]
            add_i += 1

    open(txt_file, "a").write(text)
