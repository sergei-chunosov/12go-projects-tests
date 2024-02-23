def get_number_of_trip(response, trip_key):
    i = 1
    while True:
        if response.json()['trips'][i]['segments'][0]['trip_id'] == trip_key:
            break
        i += 1
        return i
