# convert an image QR code to the text it represents
# requires the pyzbar package
# A well-cropped image of the QR code should be the first argument to this script
# e.g., $python qr_code_script.py name_of_qr_code.png


from pyzbar.pyzbar import decode
from PIL import Image
import sys

decodeQR = decode(Image.open(str(sys.argv[1])))
print(decodeQR[0].data.decode('ascii'))
