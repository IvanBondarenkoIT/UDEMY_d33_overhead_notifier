from email_manage import send_email
from sunsettime import is_night_now
from isstracker import is_iss_close
import config
from kanyequote import KanyeQuote


if __name__ == "__main__":
    if is_night_now() and is_iss_close(config.MY_LAT, config.MY_LONG):
        send_email(subject="Iss is close!", massage="Look UP!")

    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    # KanyeQuote("https://api.kanye.rest")
