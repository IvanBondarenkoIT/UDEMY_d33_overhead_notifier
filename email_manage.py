from smtplib import SMTP
from config import gmail_smtp, my_email, app_password


def send_email(to_email: str = my_email, subject: str = "", massage: str = "") -> None:
    with SMTP(gmail_smtp) as connection:
        connection.starttls()
        connection.login(user=my_email,
                         password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject:{subject}\n\n{massage}")

