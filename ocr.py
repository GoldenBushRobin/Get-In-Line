from tesserocr import PyTessBaseAPI

images = []
for i in range(1,22):
    prefix = "training-strips/cartoon"
    images.append(f'{prefix}{i}.png')
index = 1
with PyTessBaseAPI(path = '{Path to folder containing the .traineddata files}') as api:
    for img in images:
        api.SetImageFile(img)
        out = api.GetUTF8Text()

        file = open(f"outputs/tessenocr-out{index}.txt","w")
        index += 1
        file.write(out.upper())
        file.close

