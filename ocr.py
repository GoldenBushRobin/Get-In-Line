from tesserocr import PyTessBaseAPI

images = []
for i in range(1,22):
    prefix = "training-strips/cartoon"
    images.append(f'{prefix}{i}.png')
index = 1
with PyTessBaseAPI(path = 'C:\\Users\\achau\\Desktop\\datathon\\getinline\\tessdata_best-main') as api:
    for img in images:
        api.SetImageFile(img)
        out = api.GetUTF8Text()

        file = open(f"outputs/tessenocr-out{index}.txt","w")
        index += 1
        file.write(out.upper())
        file.close

