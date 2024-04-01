# PDF Slurp - Command-Line PDF Text and Image Extractor

## Description

PDF Slurp is my simple yet effective command-line tool specially tailored to pull text and images from PDF files. It's been primarily created to assist with personal knowledge development and learning. My intention behind creating PDF Slurp was to conveniently pull pages I've recently read into LLMs (and other AIs) for summarisation, flash card creation, etc. Whether you're compiling notes, building a personal knowledge base, or just satisfying your curiosity, PDF Slurp stands out as a handy assistant in your daily intellectual endeavors.

This tool is proudly homemade (mostly by Claude-3-Opus and GPT-4) and hosted here for anyone to clone and use. I've set it up for `pipx` installation because, frankly, I'm a bit too lazy to navigate the official PyPI distribution process, and I prefer the simplicity of installing it directly from a local source.

## Features

- Extract text from designated pages or ranges in a PDF, perfect for piecing together your own distilled summaries or reflections.
- Extract all text from PDFs, enabling quick access to content without manual copying and pasting.
- Pull individual images from PDFs, useful for saving diagrams, charts, or artwork that sparks inspiration.
- Invert the colors of extracted images on the fly, because why not have fun with some customization?

## Requirements

- Python 3.6 or higher
- PyPDF2
- Pillow (PIL Fork)

## Installation

To get PDF Slurp up and running on your system, `pipx` is the way to go. It's straightforward and keeps things tidy by installing the tool in an isolated environment, which is ideal for casual toolmakers and users like me. Here's how to do it:

1. Make sure `pipx` is installed on your machine. If it's not, you can get it set up with:
   ```sh
   python3 -m pip install pipx
   python3 -m pipx ensurepath
   ```

2. Head on over to the root directory where `pdf_slurp` lives and install with:
   ```sh
   pipx install .
   ```

After that, you should be good to go. Launch PDF Slurp from anywhere in your terminal and enjoy the effortless data extraction!

## Usage

Here are a few quick examples to show what PDF Slurp can do:

To extract text from pages 1 to 3 and page 5:
```sh
pdf-slurp /path/to/pdf -p 1-3,5
```

To extract all text from a PDF:
```sh
pdf-slurp /path/to/pdf --all-pages
```

To grab the third image from page 2:
```sh
pdf-slurp /path/to/pdf -p 2 -i 3
```

To invert the colors of the extracted image:
```sh
pdf-slurp /path/to/pdf -p 2 -i 3 -v
```

## License

PDF Slurp is made available under the MIT License. For more details, check out the LICENSE file on the GitHub repository.

Happy learning and managing your PDFs!
