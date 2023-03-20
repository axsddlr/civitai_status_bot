import requests


def get_uptime_list():
    url = "https://status.civitai.com/api/status-page/heartbeat/public"
    payload = ""
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/110.0.0.0"
                      "Safari/537.36 Edg/110.0.1587.56"
    }
    response = requests.get(url, data=payload, headers=headers)
    return response.json()["uptimeList"]


def process_uptime_list():
    uptime_list = get_uptime_list()
    renamed_dict = {
        "2_24": "Database",
        "3_24": "Model Scanner",
        "4_24": "Model Scanner Large",
        "5_24": "Discord Notification Server",
        "7_24": "Main Site",
        "8_24": "API"
    }
    percentage_dict = {}
    for key, value in uptime_list.items():
        if key in renamed_dict:
            new_key = renamed_dict[key]
            percentage = round(value * 100, 2)
            percentage_dict[new_key] = f"{percentage}%"
    print(percentage_dict)


process_uptime_list()
