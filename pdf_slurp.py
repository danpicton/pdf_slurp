import argparse
from PyPDF2 import PdfReader
from PIL import Image, ImageOps
import io
import sys

def extract_pages(pdf_path, page_numbers):
    """Extract specified pages from a PDF and return their text content.

    Args:
        pdf_path: A string path to the PDF file.
        page_numbers: A list of integers representing the page numbers to extract.

    Returns:
        A list of tuples, each containing a page number and its extracted text.
    """
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        extracted_pages = []

        for page_number in page_numbers:
            if page_number < 1 or page_number > len(reader.pages):
                sys.stderr.write(f"Page {page_number} not found in the PDF.\n")
                continue
            
            page = reader.pages[page_number - 1]
            text = page.extract_text()
            extracted_pages.append((page_number, text))
        
        return extracted_pages

def extract_all_text(pdf_path):
    """Extract all text from a PDF.

    Args:
        pdf_path: A string path to the PDF file.

    Returns:
        A string containing all text extracted from the PDF.
    """
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        return text

def extract_image(pdf_path, page_number, image_number, image_invert):
    """Extract a specific image from a given page in a PDF.

    Args:
        pdf_path: A string path to the PDF file.
        page_number: An integer representing the page number.
        image_number: An integer representing the image index on the page.
        image_invert: A boolean indicating whether to invert the image colors.

    Returns:
        A PIL Image object of the extracted image, or None if the image can't be found.
    """
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)

        if page_number < 1 or page_number > len(reader.pages):
            sys.stderr.write(f"Page {page_number} not found in the PDF.\n")
            return None
        
        page = reader.pages[page_number - 1]
        images = page.images

        if image_number < 1 or image_number > len(images):
            sys.stderr.write(f"Image {image_number} not found on page {page_number}.\n")
            return None
        
        image_info = images[image_number - 1]
        image_data = image_info.data
        image_stream = io.BytesIO(image_data)
        pil_image = Image.open(image_stream)

        if pil_image.mode == 'CMYK':
            pil_image = pil_image.convert('RGB')
        if image_invert:
            pil_image = ImageOps.invert(pil_image)
        
        return pil_image

def parse_page_numbers(page_numbers_str):
    """Parse page numbers/ranges from a string into a sorted list of unique page numbers.

    Args:
        page_numbers_str: A string containing page numbers and/or ranges (e.g., "1,3-5").

    Returns:
        A sorted list of unique page numbers.
    """
    page_numbers = []
    for part in page_numbers_str.split(','):
        if '-' in part:
            start, end = part.split('-')
            page_numbers.extend(range(int(start), int(end) + 1))
        else:
            page_numbers.append(int(part))
    return sorted(set(page_numbers))

def main():
    """The main function that parses arguments and performs text or image extraction based on the input."""
    parser = argparse.ArgumentParser(description='PDF Extraction Tool')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-p', '--pages', help='Page numbers to extract (e.g., 1-5,7,10)')
    parser.add_argument('-i', '--image', type=int, help='Image number to extract')
    parser.add_argument('-v', '--invert', action='store_true', help='Invert the extracted image')
    parser.add_argument('-a', '--all-pages', action='store_true', help='Extract all pages from the PDF')

    args = parser.parse_args()

    if args.all_pages:
        total_pages = extract_all_text(args.pdf_path)
        sys.stdout.write(total_pages)
        sys.stdout.flush()
    
    elif args.pages:
        page_numbers = parse_page_numbers(args.pages)
        extracted_pages = extract_pages(args.pdf_path, page_numbers)
        
        for page_number, page_content in extracted_pages:
            sys.stdout.write(f"Content of page {page_number}:\n")
            sys.stdout.write(page_content)
            sys.stdout.write('\n\n')

    if args.image and args.pages:
        page_number = page_numbers[0]  # Extract image from the first page in the list
        image = extract_image(args.pdf_path, page_number, args.image, args.invert)

        if image:
            image.save(sys.stdout.buffer, format='PNG')
        else:
            sys.stderr.write(f"Image {args.image} not found on page {page_number}.\n")

if __name__ == '__main__':
    main()