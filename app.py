from docx import Document

document = Document("before.docx")

for paragraph in document.paragraphs:
    # pragraph.runs: Retain font's style which convert before
    inline = paragraph.runs
    for i in range(len(inline)):
        inline[i].text = inline[i].text.replace("place", "replace")

document.save("after.docx")
