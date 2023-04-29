class EmailSender():
    
    def enviarEmail(self,email, senha, html_text, to_email, subject):
        import smtplib
        from email.message import EmailMessage


        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = to_email
        msg.add_alternative(f"""
            \
        {html_text}
        """, subtype='html')

        port_number = 465
        with smtplib.SMTP_SSL('smtp.gmail.com',port_number) as smtp:
            smtp.login(email, senha)
            smtp.send_message(msg)