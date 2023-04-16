from apimanage import ApiManage


def is_iss_close(my_lat: float, may_long: float):

    data = ApiManage(url='http://api.open-notify.org/iss-now.json').get_json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_longitude, iss_latitude)
    # Your position is within +5 or -5 degrees of the ISS position.
    return (my_lat - 5 <= iss_longitude <= my_lat + 5) and (may_long - 5 <= iss_longitude <= may_long + 5)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
