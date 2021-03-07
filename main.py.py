import os
import requests
import schedule
import time

index = {'count': 0}


def func(index):
    url = 'https://opendata.saemes.fr/explore/dataset/places-disponibles-parkings-saemes/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
    r = requests.get(url)

    with open(os.path.join(r"file%s.csv" % index['count']), 'wb') as f:
        f.write(r.content)
        print("File downloaded")

    index['count'] += 1


schedule.every(3).minutes.do(func, index)

while True:
    schedule.run_pending()
    time.sleep(2)
