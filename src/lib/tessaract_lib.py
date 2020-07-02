import pdf2image
from PIL import Image
from tesserocr import PyTessBaseAPI, RIL, PSM

api = PyTessBaseAPI()

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)


def ocr_core(img):
    
    api.SetImage(img)
    text = api.GetUTF8Text()
    confidence = api.AllWordConfidences()
    return text, confidence

def get_component(img):
    api.SetImage(img)
    boxes = api.GetComponentImages(RIL.TEXTLINE, True)
    print('Found {} textline image components.'.format(len(boxes)))
    for i, (im, box, _, _) in enumerate(boxes):
        # im is a PIL image object
        # box is a dict with x, y, w and h keys
        api.SetRectangle(box['x'], box['y'], box['w'], box['h'])
        ocrResult = api.GetUTF8Text()
        conf = api.MeanTextConf()
        print(box)
        print(u"Box[{0}]: x={x}, y={y}, w={w}, h={h}, "
              "confidence: {1}, text: {2}".format(i, conf, ocrResult, **box))

def orientation_detection(img):
    api.SetImage(img)
    api.Recognize()

    it = api.AnalyseLayout()
    orientation, direction, order, deskew_angle = it.Orientation()
    print("Orientation: {:d}".format(orientation))
    print("WritingDirection: {:d}".format(direction))
    print("TextlineOrder: {:d}".format(order))
    print("Deskew angle: {:.4f}".format(deskew_angle))


def run_ocr(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        # orientation_detection(img)
        get_component(img)
        # print(text)
        # print(confidence)
        print("********************************************************")

