import smtplib

MY_EMAIL_PASSWORD = "wciannkbjszizitm"
MY_EMAIL = "salihyos2019@gmail.com"


def via_email(message:str, address):
    message = message.replace("\n", "")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=address,
                            msg=f"Subject:This is a secret message\n\n{message}",
                            )