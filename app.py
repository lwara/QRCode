import psutil as psutil
import qrcode
import psutil
from psutil._common import bytes2human

import psutil._common

#sample data
input_RAM_used = "RAM % Space Used :", psutil.virtual_memory()
input_HDD_toa = "got it "

#Create QR Code Instance

qr = qrcode.QRCode(version=1, box_size=10, border=5)
#qr.add_data(input_RAM_used)

def get_RAM_details(ram):
    qr.add_data("MEMORY\n")
    for name in ram._fields:
        value = getattr(ram, name)
        if name != 'percent':
            value = bytes2human(value)
        add_QR_data('%-10s : %7s' % (name.capitalize(), value))

def get_disk_usage(disk_space):
    qr.add_data("DISK SPACE\n")
    for name in disk_space._fields:
        value = getattr(disk_space, name)
        if name != 'percent':
            value = bytes2human(value)
        add_QR_data(value)






def add_QR_data(input_data):
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')

def main():
    print('MEMORY\n------')
    get_RAM_details(psutil.virtual_memory())
    get_disk_usage(psutil.disk_usage('/'))

if __name__ == '__main__':
    main()