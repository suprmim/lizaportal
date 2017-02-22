import logging
import smtplib
from gsettings import settings

def send_email(email, body, subject=''):
    if settings.EMAIL_SMTP_SENDER is None:
        raise Exception('No EMAIL_SMTP_SENDER in flaskcbv settings')
    if settings.EMAIL_SMTP_LOGIN is None or settings.EMAIL_SMTP_PASSWD is None:
        raise Exception('No EMAIL_SMTP_LOGIN or EMAIL_SMTP_PASSWD in flaskcbv settings')
    if settings.EMAIL_SMTP_SERVER is None or settings.EMAIL_SMTP_PORT is None:
        raise Exception('No EMAIL_SMTP_SERVER or EMAIL_SMTP_PORT in flaskcbv settings')

    try:
        s_ = smtplib.SMTP(settings.EMAIL_SMTP_SERVER, settings.EMAIL_SMTP_PORT)
    except Exception as err:
        logging.error("SMTP: Can't connect to server: %s:%s: %s" % (settings.EMAIL_SMTP_SERVER, settings.EMAIL_SMTP_PORT, err))

    ## Start TLS security:
    if hasattr(settings, 'EMAIL_SMTP_TLS') and settings.EMAIL_SMTP_TLS:
        s_.starttls()

    ## Server auth and sending mail:
    s_.login(settings.EMAIL_SMTP_LOGIN, settings.EMAIL_SMTP_PASSWD)

    content = u"""\
From: %(sender)s
Subject: %(subject)s

%(body)s
    """ % {
        'sender': settings.EMAIL_SMTP_SENDER,
        'subject': subject,
        'body': body,
    }
    s_.sendmail(settings.EMAIL_SMTP_SENDER, email, content)
    s_.quit()

