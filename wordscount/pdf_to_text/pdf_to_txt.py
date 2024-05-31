import os

from pypdf import PdfReader


# to pdf
def get_pdf_files_from_dir():
    pdf_sources_dir = os.path.dirname(os.path.dirname(__file__))
    for _ in range(3):
        pdf_sources_dir = os.path.dirname(pdf_sources_dir)

    pdf_sources_dir = os.path.join(pdf_sources_dir, 'pdfsourcetest')  #TBD
    return pdf_sources_dir


path = get_pdf_files_from_dir()
pdf_file_path = os.path.join(path, "example.pdf")
reader = PdfReader(pdf_file_path)
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

print(text)
