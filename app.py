import flask
import psutil as psutil
import qrcode
import psutil
from psutil._common import bytes2human
from flask import Flask, render_template
import psutil._common

app = Flask(__name__)


#sample data
input_RAM_used = "RAM % Space Used :", psutil.virtual_memory()

#Create QR Code Instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

def get_RAM_details(ram):
    qr.add_data("MEMORY\n")
    for name in ram._fields:
        value = getattr(ram, name)
        if name != 'percent':
            value = bytes2human(value)
        add_QR_data('%-10s : %7s' % (name.capitalize(), value)+'\n')

def get_disk_usage(disk_space):
    qr.add_data("DISK SPACE\n")
    for name in disk_space._fields:
        value = getattr(disk_space, name)
        if name != 'percent':
            value = bytes2human(value)
        add_QR_data('%-10s : %7s' % (name.capitalize(), value)+'\n')






def add_QR_data(input_data):
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')

@app.route('/getQrImage')
def get_image():
    image_name = 'qrcode001.png'
    #Simage_name.Seek(0)
    return flask.send_file(image_name, mimetype='png')


def main():
    get_RAM_details(psutil.virtual_memory())
    get_disk_usage(psutil.disk_usage('/'))
    get_image()



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    #main()

