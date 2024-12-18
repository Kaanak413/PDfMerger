from pypdf import PdfWriter
import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

def main():
    # Suppress the root tkinter window
    Tk().withdraw()

    messagebox.showinfo("Information", "Select PDF files to merge. Press 'Cancel' to stop.")

    pdfs = []
    while True:
        filename = askopenfilename(filetypes=[("PDF Files", "*.pdf")], title="Select a PDF file")
        if not filename:  # Stop when the user cancels the dialog
            break
        pdfs.append(filename)
    
    if not pdfs:
        messagebox.showwarning("Warning", "No files selected. Exiting.")
        return

    # Output file selection
    output_file = asksaveasfilename(
        defaultextension=".pdf", 
        filetypes=[("PDF Files", "*.pdf")],
        title="Save Merged PDF As"
    )
    if not output_file:
        messagebox.showwarning("Warning", "No output file specified. Exiting.")
        return

    try:
        writer = PdfWriter()
        for pdf in pdfs:
            with open(pdf, "rb") as f:
                writer.append(f)
        with open(output_file, "wb") as output:
            writer.write(output)
        messagebox.showinfo("Success", f"Merged PDF saved as: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    main()
