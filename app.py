from docx import Document

document = Document("before.docx")

for paragraph in document.paragraphs:
    # 変換前のstyle(フォントなど)を維持する
    inline = paragraph.runs
    for i in range(len(inline)):
        inline[i].text = inline[i].text.replace("置換前", "置換後")

document.save("after.docx")
