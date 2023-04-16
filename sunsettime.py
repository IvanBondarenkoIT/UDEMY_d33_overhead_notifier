import config
from apimanage import ApiManage
from datetime import datetime


def double_split(data, first_split_ch: str, second_split_ch: str):
    return data.split(first_split_ch)[1].split(second_split_ch)


def is_night_now() -> tuple:
    parameters = {
        "lat": config.MY_LAT,
        "lng": config.MY_LONG,
        "formatted": 0,
    }

    data = ApiManage(url='https://api.sunrise-sunset.org/json',
                     params=parameters).get_json()

    time_now = int(double_split(str(datetime.now()), " ", ":")[0])
    sunrise = int(double_split(data["results"]["sunrise"], "T", ":")[0])
    sunset = int(double_split(data["results"]["sunset"], "T", ":")[0])

    return sunset <= time_now or time_now <= sunrise


print(is_night_now())

