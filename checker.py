import json
import requests
from concurrent.futures import ThreadPoolExecutor

PLAYLIST_URLS = [
    "https://iamshajon.com/playlist/fifa.json",
    "https://iamshajon.com/playlist/sports.json",
    "https://iamshajon.com/playlist/bangla.json",
    "https://iamshajon.com/playlist/channels.json"
]

def check_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        # ৫ সেকেন্ডের মধ্যে রেসপন্স না পেলে ফেইল ধরে নেবে
        response = requests.get(url, headers=headers, timeout=5, stream=True)
        return url, response.status_code == 200
    except:
        return url, False

def main():
    all_channels = []
    for p_url in PLAYLIST_URLS:
        try:
            res = requests.get(p_url)
            all_channels.extend(res.json())
        except Exception:
            pass

    unique_urls = list(set([ch.get("url") for ch in all_channels if ch.get("url")]))
    health_data = {}
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_url, unique_urls)
        for url, is_working in results:
            health_data[url] = {"status": "ok"} if is_working else {"status": "fail"}
                
    with open("health.json", "w") as f:
        json.dump(health_data, f, indent=4)

if __name__ == "__main__":
    main()
