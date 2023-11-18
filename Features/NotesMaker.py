import PyPDF2

# Open the PDF file using a raw string
pdf_file_path = r'D:\MyData\Documents\CODING\Python\Jarvis\Data\PDFs\iesc101.pdf'
pdf_file = open(pdf_file_path, 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extract text from each page
text = ''
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text += page.extract_text()

# Close the PDF file
pdf_file.close()

# Create or open a new text file to write the extracted text
output_file_path = r'D:\MyData\Documents\CODING\Python\Jarvis\DataBase\Notes.txt'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(text)

print(f'Text extracted from {pdf_file_path} and saved to {output_file_path}')
