import qrcode

from PIL import Image


# Taking UPI ID as a input\
upi_id = input('Enter UPI ID = ')

#upi://pay?pa=UPI_ID&apn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

# Defining payment URL based on the UPI ID and the payment app
# You can modify these URLs based on the payment apps you want to support


phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"


# Create QR codes for each app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR code to image file

phonepe_qr.save('phonepe.png')
paytm_qr.save('paytm.png')
google_pay_qr.save('google_pay.png')

# Display the QR codes (You may need to install the pillow library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()