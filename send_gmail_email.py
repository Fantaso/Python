import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = 'envia@gmail.com'
toaddr = "recibe@mail.com"
msg = MIMEMultipart('alternative')
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Titulo del email"
 
body = "Hola soy solo texto simple" #si el servidor no acpeta codigo html este sera el mensaje
html = """\
<html>
  <head></head>
  <body>
    <h4>Yo si soy codigo html, si el servidor acepta mostrar codigo html</h4>
  </body>
</html>
"""
msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(html, 'html'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "aqui_va_la_clave_de_envia@mail.com")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
