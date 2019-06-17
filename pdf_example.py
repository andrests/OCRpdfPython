import io
import time

import pytesseract
from PIL import Image
from wand.image import Image as wi

start = time.time()

pdf = wi(filename="data/data.pdf", resolution=100)
pdfImage = pdf.convert('jpeg')

for idx, img in enumerate(pdfImage.sequence):
    print('\n>>> PÁGINA #{}:'.format(idx + 1))
    print(pytesseract.image_to_string(Image.open(io.BytesIO(wi(image=img).make_blob('jpeg'))), lang='spa'))

print("\n>>>>>>>>>> PROCESS TIME: " + str(time.time() - start))