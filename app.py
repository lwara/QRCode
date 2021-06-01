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




def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))
        qr.add_data('%-10s : %7s' % (name.capitalize(), value))
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode001.png')


def main():
    print('MEMORY\n------')
    pprint_ntuple(psutil.virtual_memory())
    #print('\nSWAP\n----')
    #pprint_ntuple(psutil.swap_memory())


if __name__ == '__main__':
    main()