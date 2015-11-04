from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
import re
from smtplib import SMTP

# Example use:
# import mailer
# e = mailer.Email(mailing_list=["geraint@geraintanderson.com"], body="bod", subject="Subject line", attachments=["/tmp/a.txt", "/tmp/b.txt", "/tmp/c.txt", "/tmp/d.txt"])
# e.see_details()
# e.send_mail()

class Email:
    """A class to create emails"""
    def __init__(self, mailing_list=[], body="", subject="", attachments=[], from_email="geraint@geraintanderson.com"):
        """Define the object"""
        self.mailing_list = []
        self.add_recipient(mailing_list)
        self.body = body
        self.subject = subject
        self.attachments = attachments
        if self.validate_email(from_email):
            self.from_email = from_email
        else:
            print "From email address is invalid"

    def add_recipient(self, recipients):
        '''Used to add recipients'''

        if isinstance(recipients, basestring):
            if self.validate_email(recipients):
                self.mailing_list.append(recipients)
        elif isinstance(recipients, list):
            for recipient in recipients:
                if self.validate_email(recipient) and isinstance(recipient, basestring):
                    self.mailing_list.append(recipient)
                else:
                    print "Email address must be in the format xxx@yyy.zzz"
        else:
            print "Email address must be a string, or a list of strings in the format xxx@yyy.zzz"


    def validate_email(self, email):
        """Used to validate an email address and returns a boolean"""
        if bool(re.search('.+@.+\..+', email)):
            return True

    def see_details(self):
        """View the message details"""
        for recipient in self.mailing_list:
            print "Recipient: " + recipient
        print "Body: " + self.body
        print "Subject: " + self.subject
        for file in self.attachments:
            print "attachments: " + file
        print "from_email: " + self.from_email
        

    def send_mail(self):
        """Used to send the email."""
    
        # Set up the message basics
        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = ', '.join(self.mailing_list)
        msg['Subject'] = self.subject
    
        print msg
        # Set the message body
        msg.attach(MIMEText(self.body))
    
        # Process attachments
        for filename in self.attachments:
            with open(filename, "rb") as f:
                msg.attach(MIMEApplication(
                    f.read(),
                    Content_Disposition='attachment; filename="%s"' % basename(filename),
                    Name=basename(filename)
                ))
    

        # Configure and send the mail
        s = SMTP('localhost')
        s.sendmail(self.from_email, self.mailing_list,  msg.as_string())
        s.close()
