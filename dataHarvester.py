import sys
import cv2
from PIL import Image
import pytesseract
import numpy as np


outputFile = "ayy2.png"
inputFile = "data/img0090.jpg"


im = cv2.imread(inputFile)

imR = im[:,:,2]
ret, imR = cv2.threshold(imR, 220, 255, cv2.THRESH_BINARY)
invImR = 255-imR
invImRSlice = invImR[:200, :]
cv2.imwrite(outputFile, invImRSlice)
cv2.imshow(outputFile,invImRSlice)
cv2.imshow(inputFile,im)
cv2.waitKey(0)
cv2.destroyAllWindows()


print(sys.argv)

inputFile
    
try :
    tesS = pytesseract.image_to_string(Image.open(outputFile))
except:
    print("shizz didnt work")
print(f"output string: \"{tesS}\"    len: {len(tesS)}   fileLoc {inputFile}")


input("")