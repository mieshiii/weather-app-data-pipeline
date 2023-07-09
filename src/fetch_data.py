import requests
import json
import datetime as dt
import taosrest


def get_data(location: str, conn: str):
	# create api request
	payload = {'Key': '16734c31aa2c448ca08145152230907', 'q': location , 'aqi': 'yes'}
	r = requests.get("http://api.weatherapi.com/v1/current.json", params=payload)
	r_string = r.json()
	current = r_string['current']
	origin_time = dt.datetime.strptime(current['last_updated'], '%Y-%m-%d- %H:%M')
	current['last_updated'] = origin_time.strftime('%Y-%m-%dT%H:%M:%SZ')
