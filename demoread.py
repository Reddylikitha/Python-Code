import os

def read_text_file(file_path):
    with open(file_path.strip('"'), 'r') as file:
            content = file.read()
            print(f"Content of the file:\n{content}")
if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")
    read_text_file(file_path)