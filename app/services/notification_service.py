import requests
from utils.session_utils import log_to_session

def send_push_notification(
    api_key, 
    app_id, 
    message_pt, 
    message_en, heading_en, heading_pt, all_users, external_id, small_icon, launch_url,):
    url = "https://api.onesignal.com/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Basic {api_key}"
    }

    data = {
        "app_id": app_id,
        "contents": {"en": message_en, "pt": message_pt},
        "headings": {"en": heading_en, "pt": heading_pt},
        "small_icon": small_icon,
        "url": launch_url,
        "target_channel": "push"
    }

    if all_users == 'on':
        data.update({"included_segments": ["All"]})
    elif external_id:
        data.update({"include_aliases": {"external_id": [external_id]}})

    try:
        response = requests.post(url, headers=headers, json=data)
        log_to_session(f"{response.status_code} {response.json()}")
        return response.status_code, response.json()
    except requests.exceptions.RequestException as e:
        log_to_session(f"RequestException: {str(e)}")
        return 500, {"errors": str(e)}

def get_messages_from_api(api_key, app_id):
    url = f"https://onesignal.com/api/v1/notifications?app_id={app_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {api_key}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            notifications = response.json().get('notifications', [])
            messages = [{"text": n.get("contents", {}).get("en", "Mensagem sem conteúdo")} for n in notifications]
            log_to_session(f"{messages}")
            return {"messages": messages}, 200
        else:
            log_to_session(f"Failed to retrieve messages - Status Code: {response.status_code}")
            return {"error": "Failed to retrieve messages."}, response.status_code
    except requests.exceptions.RequestException as e:
        log_to_session(f"RequestException: {str(e)}")
        return {"error": "Request failed due to an exception."}, 500
