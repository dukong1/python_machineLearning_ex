import qrcode

qr_data = 'https://github.com/dukong1/python_machineLearning_ex.git'
qr_img = qrcode.make(qr_data)

save_path = '4. QR코드 생성기\\' + qr_data + '.png'
qr_img.save(save_path)
