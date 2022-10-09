import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = '{file path to tesseract.exe}'
img = cv2.imread("sample.png")
boxes = pytesseract.image_to_boxes(img)
text = pytesseract.image_to_string(img)

print(text)
print(boxes)

lines = []
line = ''
box_lines = boxes.split('\n')
boxes = []
for box_line in box_lines:
    if len(box_line) != 0 and box_line[0] != '~':
        boxes.append(box_line.split(' '))

print(len(boxes))
width = int(boxes[0][3])
height = int(boxes[0][2])
tot_line_height = 0
chars_in_line = 0
avg_heights = []

for box in boxes:
#    print(box)
    if(abs(height - int(box[2])) > 14):
        lines.append(line)
        line = ''
        if(chars_in_line != 0):
            avg_heights.append(tot_line_height/chars_in_line)
        tot_line_height = 0
        chars_in_line = 0
    if(int(box[1]) - width > 4):
        line += ' '
    line += box[0]
    if(box[0] >= 'A' and box[0] <= 'z'):
        tot_line_height += (int(box[2]) + int(box[4]))/2
        chars_in_line += 1
    height = int(box[2])
    width = int(box[3])
for l in lines:
    print(l)
for x in avg_heights:
    print(x)
print(line)