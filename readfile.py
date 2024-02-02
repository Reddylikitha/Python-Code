import os
import json
import csv
import pandas as pd
from PyPDF2 import PdfReader 
import nltk
from nltk.tokenize import word_tokenize 

nltk.download('punkt')

def custom_tokenizer(text):
    tokens = word_tokenize(text)
    return tokens


def read_file(file_path,tokenizer=custom_tokenizer):
   
    file_extension = os.path.splitext(file_path)[1].lower()
    print("file extension :",file_extension)

#For reading text file
    if file_extension == '.txt':
        print("Reading a text file...")
        with open(file_path, 'r') as file:
            content = file.read()
            tokens = tokenizer(content)
            print(f"Number of tokens: {len(tokens)}")
            # print(content)
    
#For reading pdf file
    elif file_extension == '.pdf':
        print("Reading a pdf file...")
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                tokens = tokenizer(page.extract_text())
                print(f"Number of tokens in page {page_num + 1}: {len(tokens)}")
                # print(page.extractText())


#For reading CSV file
    elif file_extension == '.csv':
        print("Reading a csv file...")
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                 tokens = tokenizer(' '.join(row))
                 print(f"Number of tokens: {len(tokens)}")
                # print(row)
    
#For reading json file
    elif file_extension == '.json':
        print("Reading a json file...")
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            tokens = tokenizer(json.dumps(data))
            print(f"Number of tokens: {len(tokens)}")
            # print(data)
        
#For reading excel files
    elif file_extension in ['.xlsx', '.xls']:
        print("Reading a excel file...")
        df = pd.read_excel(file_path)
        tokens = tokenizer(df.to_string())
        print(f"Number of tokens: {len(tokens)}")
        # print(df)


    else:
        print(f"Unsupported file type: {file_extension}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file: ")
    print(f"File path entered: {file_path}")
    read_file(file_path.strip('"'))



