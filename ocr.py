from tesserocr import PyTessBaseAPI

images = ['training-strips/cartoon3.png']

with PyTessBaseAPI(path = 'C:\\Users\\achau\\Desktop\\datathon\\getinline\\tessdata_best-main') as api:
    for img in images:
        api.SetImageFile(img)
        out = api.GetUTF8Text()
print(out.upper())

