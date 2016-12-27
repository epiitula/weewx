#!/usr/bin/env python2

def check_and_repair(received_data):

    weather_range = {"inTemp":              {'start': -50,  'end': 70}, 
                     "outTemp":             {'start': -50,  'end': 70},
                     "outHumidity":         {'start': 0,    'end': 100},
                     "windSpeed":           {'start': 0,    'end': 200},
                     "windDir":             {'start': 0,    'end': 360},
                     "pressure":            {'start': 0,    'end': 1500},
                     "deltarain":           {'start': 0,    'end': 100},
                     "illumination":        {'start': 0,    'end': 3000},
                     "geiger":              {'start': 0,    'end': 1000},
                     "maxWind":             {'start': 0,    'end': 200}
                     }

    for param in received_data:

        try:
            if weather_range[param]['start'] <= received_data[param] <= weather_range[param]['end']:
                 pass
            else:
                received_data[param] = None

        except KeyError:
            pass

    return received_data