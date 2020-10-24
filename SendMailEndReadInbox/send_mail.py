import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Not secure
username='test@gmail.com'
password='mmmmmmmmmm123'

def send_mail(text='Email Body',subject='Hello',from_email='MMO<test@gmail.com>' ,to_emails=None,html=None):
    assert isinstance(to_emails,list)
    msg=MIMEMultipart('alternative')
    msg["From"]=from_email
    msg["To"]=to_emails
    msg["Subject"]=subject

    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)


    html_part=MIMEText('<h1>asdasdasd</h1>','html')
    msg.attach(html_part)

    msg_str=msg.as_string()

    server=smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()

# familiar to c# using scope
    # with smtplib.SMTP() as server: 
    #     server.login()
    #     pass















#    mlist=["123","324","asda"]
    # ",".join(mlist) -> samp: 123,324,asda