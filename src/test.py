import pdf2image
from PIL import Image
from tesserocr import PyTessBaseAPI


def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(img):
    api = PyTessBaseAPI()
    api.SetImage(img)
    text = api.GetUTF8Text()
    confidence = api.AllWordConfidences()
    return text, confidence


def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    print(images)
    for pg, img in enumerate(images):
        text, confidence = ocr_core(img)
        print(text)
        print(confidence)
        print("********************************************************")


print_pages('Form-Original-1-9.pdf')