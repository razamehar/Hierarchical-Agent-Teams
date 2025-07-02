from fpdf import FPDF
from docx import Document
import datetime
import os
from langchain_core.tools import tool
from schema.schema import FileFormat


@tool
def save_doc_tool(file_format: FileFormat, content: str):
    """
    Saves the provided content into a document file in either PDF or DOC format.
    The file is saved inside an 'output' folder with a timestamped filename.
    """

    os.makedirs("output", exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    ext = file_format.format.lower()
    filename = f"output/document_{timestamp}.{ext}"

    if ext == "pdf":
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in content.split('\n'):
            pdf.cell(0, 10, line, ln=True)
        pdf.output(filename)
        return f"PDF saved successfully at {filename}"

    elif ext == "doc" or ext == "docx":
        doc = Document()
        for line in content.split('\n'):
            doc.add_paragraph(line)
        doc.save(filename)
        return f"DOC saved successfully at {filename}"

    else:
        return "Unsupported file format. Please use 'pdf' or 'doc'."