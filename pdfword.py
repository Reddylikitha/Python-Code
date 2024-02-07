
import PyPDF2
import docx
import os

def pdf_to_text_converter(pdf_path, output_text_file):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    
    with open(output_text_file, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

def word_to_text_converter(docx_path, output_text_file):
    doc = docx.Document(docx_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'

    with open(output_text_file, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

def main():
    input_file_path = input("Enter the path of the PDF or Word file: ").strip('"')

    file_name, file_extension = os.path.splitext(input_file_path)

    if file_extension.lower() == '.pdf':
        output_text_file = f"{file_name}.txt"
        pdf_to_text_converter(input_file_path, output_text_file)
        print(output_text_file)
        print("PDF to text conversion complete.")
    
    elif file_extension.lower() == '.docx':
        output_text_file = f"{file_name}.txt"
        word_to_text_converter(input_file_path, output_text_file)
        print(output_text_file)
        print("Word to text conversion complete.")
    
    else:
        print("Unsupported file format. Please provide a correct file format.")

if __name__ == "__main__":
    main()
