from email.mime.text import MIMEText
import smtplib


# plain 表明纯文本 utf-8多语言兼容
msg = MIMEText('hello, send by python', 'plain', 'utf-8')
from_addr = input('from:')
