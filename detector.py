# Import required packages
import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = '{file path to tesseract.exe}'

# Read image from which text needs to be extracted
img = cv2.imread("sample.png")

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# making kernels
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
												cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()

# Clear the output file
file = open("output.txt", "w+")
file.write("")
file.close()


for cnt in contours:
	x, y, w, h = cv2.boundingRect(cnt)
	
	# Drawing a rectangle on copied image
	rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	# Cropping the text block for giving input to OCR
	cropped = im2[y:y + h, x:x + w]
    # converted to grayscale
	crop_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# Open the file in append mode
	file = open("output.txt", "a")
	
	# Apply OCR on the cropped image
	text = pytesseract.image_to_string(crop_gray)
	
	# Appending the text into file
	file.write(text)
    
	file.write("\n")
	file.close
