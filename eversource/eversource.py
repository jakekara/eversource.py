from datetime import datetime, timedelta
import time
import requests

REGION_IDS = ["east","west","hampshire","conn"]
METADATA_URL = "https://outagemap.eversource.com/resources/data/external/interval_generation_data/metadata.json"

def get_json(url):
    resp = requests.get(url)
    assert resp.status_code == 200
    return requests.get(url).json()


def epoch_time(dt):
    """ Get the epoch string in GMT """

    offset = int(time.localtime().tm_gmtoff / 3600)

    return str((dt - datetime(1970,1,1) + timedelta(hours=offset)) / timedelta(microseconds=1))[:-5]

def epoch_now():
    """ Get the current epoch time string"""

    return epoch_time(datetime.now())

def get_metadata_url():
    return f"{METADATA_URL}?_={str(epoch_now())}"

def get_metadata():
    return get_json(get_metadata_url())

def get_report_url (region_id):
    if region_id not in REGION_IDS:
        raise Exception(f"Invalid region ID. Valid options include: {REGION_IDS}")

    directory = get_metadata()["directory"]

    url = "https://outagemap.eversource.com/resources/data/external/interval_generation_data/"\
    f"{directory}/report_{region_id}.json"

    return url

def get_report(region_id):
    url = get_report_url(region_id)
    return get_json(url)
