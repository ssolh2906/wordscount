import os

from pypdf import PdfReader

from wordscount.config import PDF_SOURCES_DIR_TEST, CONVERTED_TEXTS_DIR


# to pdf
def get_pdf_file_names_from_dir():
    pdf_sources_dir = os.path.dirname(os.path.dirname(__file__))
    for _ in range(3):
        pdf_sources_dir = os.path.dirname(pdf_sources_dir)

    pdf_sources_dir = os.path.join(pdf_sources_dir, PDF_SOURCES_DIR_TEST)

    # todo : get list of all pdf and put them in a list
    file_names = []
    for file_name in os.listdir(pdf_sources_dir):
        file_path = os.path.join(pdf_sources_dir, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.pdf'):
            file_names.append(file_path)

    return file_names


def read_pdf_files_to_string(pdf_file_name):
    reader = PdfReader(pdf_file_name)
    number_of_pages = len(reader.pages)
    text = ""
    for i in range(number_of_pages):
        page = reader.pages[i]
        text += page.extract_text()
    return text


def all_pdf_to_txt():
    print("...Reading PDF and save as txt...")
    pdf_file_names = get_pdf_file_names_from_dir()
    for pdf_file in pdf_file_names:
        save_pdf_as_txt(pdf_file)
    print("\n")


def save_pdf_as_txt(pdf_file_name):
    txt_directory = os.path.dirname(os.path.dirname(__file__))
    for _ in range(3):
        txt_directory = os.path.dirname(txt_directory)
    _string = read_pdf_files_to_string(pdf_file_name)
    txt_file_name = pdf_file_name
    for _ in range(2):
        txt_file_name = os.path.dirname(txt_file_name)
    txt_file_name = os.path.join(txt_file_name, CONVERTED_TEXTS_DIR)  # todo: exception when there is no dir
    txt_file_name = os.path.join(txt_file_name, os.path.basename(pdf_file_name) + ".txt")
    save_string_to_txt(txt_file_name, _string)


def save_string_to_txt(txt_file_name, _string):
    try:
        with open(txt_file_name, 'w', encoding='utf-8') as file:
            file.write(_string)
        print(f"String saved to '{os.path.basename(txt_file_name)}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Test
all_pdf_to_txt()
