from asia_12go_project.utils.api_requests import post_request


def get_ticket_hash():
    url = '/api/nuxt/en/cart'
    payload = {
        "trips": [
            {
                "tripId": "TH01xL01xR004a00l028QSB9",
                "datetime": "2024-02-27-06-10-00"
            }
        ],
        "fromSlug": "bangkok",
        "toSlug": "koh-samui",
        "hash": "null",
        "seats": 1
    }

    response = post_request(url, json=payload)

    return response
