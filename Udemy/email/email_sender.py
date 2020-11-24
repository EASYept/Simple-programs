import smtplib

from email.message import EmailMessage

"""TODO IT'S NOT WORKING
ERROR: 535, b'5.7.8 Error: authentication failed: This user does not have access rights to this service"""


email = EmailMessage()
email['from'] = 'easy'
email['to'] = 'easyept@gmail.com'
email['subject'] = 'You won a 1 000 000 dollars'
print('123')
email.set_content("U FUCKIN' WON!")
print('123')
with smtplib.SMTP_SSL(host='smtp.yandex.ru', port=465) as smtp:
    smtp.ehlo()
    print('123')
    smtp.login('bybl1k@yandex.ru', 'randompassword8041')
    print('123')
    smtp.send_message(email)
    print('123')
    print('Done!')





