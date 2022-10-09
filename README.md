# Get-In-Line

This project uses two different methods to take an output: using tesseract trained models on an image, and making a ground truth model and training a model to extract the text from an image.

## Tesseract Libraries
ocr.py uses tesserocr, a python api to tesseract-ocr, to extract the text.
detector.py and detector2.py both use pytesseract to extract the text, although with different filtering and extraction methods.

