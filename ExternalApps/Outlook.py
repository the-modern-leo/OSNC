from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from bs4 import BeautifulSoup
from auth import outlook

class settings():
    DEFAULT_FOOTER_HTML = ""
    DEFAULT_FOOTER = ""
    SERVER = 'smtp.umail.utah.edu'
    default_recipients = ""
    enable_tls = True

class Emailer():
    """
    Emailer module. This is a common interface to email messages and
    attachments from other modules.
    Args:
        default_recipients (list): Default recipient(s) as a list of strings.
        enable_tls (bool): Optional boolean to enable or disable SSL to the SMTP
            server. Default is True.
        test (bool): Optional boolean to enable test mode, which will return the
            message instead of sending an email. Default is False.
    """
    def __init__(self):
        self._server = settings.SERVER
        self._default_recipients = settings.default_recipients
        self._enable_tls = settings.enable_tls
        self._sm = None

    def __enter__(self):
        self._sm = SMTP(self._server)
        if self._enable_tls:
            self._sm.starttls()
        return self

    def send_email(self, subject, body, recip, sender, html=False,
            footer=None, attachment=None, filename=None):
        """
        Send an email.
        Args:
            subject (str): Subject line.
            body (str): TestEmail body.
            recip (list): Recipient email as a string (is converted to list),
                list of strings or None to use the default recipient in module
                settings.
            html (bool): Optional boolean, set True if the body and optional
                footer is HTML formatted.
            footer (str): Optional footer, if this is empty or None the default
                footer will be used.
            sender (str): Optional sender, if this is empty or None the default
                sender will be used.
            attachment (str): Optional attachment data as a base64-encodable
                string or object.
            filename (str): Optional filename for an attachment as a string. If
                attachment is given this field must be passed in.
        Returns:
            Message contents if this object's test property is True.
        """
        if attachment is not None and not filename:
            raise ValueError("Attachment missing filename")

        # format sender and recipients
        if recip is None: # send to default recipient(s)
            recip = self._default_recipients
        if isinstance(recip, str):
            recip = [recip]

        # add header/start message
        if attachment is not None: # Message with attachment
            msg = MIMEMultipart()
            msg['Subject'] = str(subject)
            msg['From'] = str(sender)
            msg['To'] = ', '.join(recip)
            if html:
                htmlbody = ("<html><head></head><body>" + str(body) +
                        "<br><br><hr>" +
                        (footer if footer else settings.DEFAULT_FOOTER_HTML) +
                        "</body></html>")
                msg.attach(MIMEText(htmlbody, 'html'))
            else:
                msg.attach(MIMEText(str(body) + '\n\n' +
                        str(footer if footer else settings.DEFAULT_FOOTER)))

            attachment = MIMEApplication(attachment, Name=filename)
            attachment['Content-Disposition'] = ('attachment; filename="' +
                    filename + '"')
            msg.attach(attachment)
        elif html: # HTML message, will send with alternate text message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = str(subject)
            msg['From'] = str(sender)
            msg['To'] = ', '.join(recip)
            htmlbody = ("<html><head></head><body>" + str(body) +"<br><br><hr>"+
                    (footer if footer else settings.DEFAULT_FOOTER_HTML) +
                    "</body></html>")

            textbody = BeautifulSoup(body, 'html.parser').get_text()
            if footer:
                textbody += ('\n\n' +
                        BeautifulSoup(footer, 'html.parser').get_text(
                        separator=' '))
            else:
                textbody += '\n\n' + settings.DEFAULT_FOOTER

            msg.attach(MIMEText(textbody, 'plain'))
            msg.attach(MIMEText(htmlbody, 'html'))
        else: # Normal, text-only message
            msg = MIMEText(str(body) + '\n\n' +
                    str(footer if footer else settings.DEFAULT_FOOTER))
            msg['Subject'] = str(subject)
            msg['From'] = str(sender)
            msg['To'] = ', '.join(recip)

        self._sm.sendmail(sender, recip, msg.as_string())

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._sm.quit()