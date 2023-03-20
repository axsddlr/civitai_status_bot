import requests


async def get_uptime_list():
    """
    It makes a request to the Civitai status page API and returns the
    uptime list
    :return: A list of dictionaries.
    """
    url = "https://status.civitai.com/api/status-page/heartbeat/public"
    payload = ""
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/110.0.0.0"
                      "Safari/537.36 Edg/110.0.1587.56"
    }
    response = requests.get(url, data=payload, headers=headers)
    return response.json()["uptimeList"]


async def process_uptime_list():
    """
    It takes the uptime list from the API, renames the keys, and returns a dictionary with the uptime percentage
    :return: A dictionary with the uptime of each service.
    """
    uptime_list = await get_uptime_list()
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
    return percentage_dict
