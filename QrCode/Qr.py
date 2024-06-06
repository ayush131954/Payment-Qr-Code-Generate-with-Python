import qrcode
upi_id=input("Enter thr upi id=")

phone_url=f'upi://pa={upi_id}&pn=Reciept%20name&mc=1234'
paytm_url=f'upi://pa={upi_id}&pn=Reciept%20name&mc=1234'
Google_pay_url=f'upi://pa={upi_id}&pn=Reciept%20name&mc=1234'

phone_qr= qrcode.make(phone_url)
paytm_qr= qrcode.make(paytm_url)
Google_pay_qr= qrcode.make(Google_pay_url)

phone_qr.save('phone_qr.png')
paytm_qr.save('paytm_qr.png')
Google_pay_qr.save('Google_pay_qr.png')

phone_qr.show()
paytm_qr.show()
Google_pay_qr.show()
