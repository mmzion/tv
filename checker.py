import json
import requests
from concurrent.futures import ThreadPoolExecutor

# আপনার প্লেলিস্টের লিংকগুলো
PLAYLIST_URLS = [
    "https://iamshajon.com/playlist/fifa.json",
    "https://iamshajon.com/playlist/sports.json"
    # প্রয়োজনে বাকিগুলো যোগ করুন
]

def check_url(url):
    try:
        # m3u8 ফাইলের জন্য GET রিকোয়েস্ট সবচেয়ে ভালো কাজ করে (হেডার্স দিয়ে)
        headers = {'User-Agent': 'Mozilla/5.0'}
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
        except Exception as e:
            print(f"Error fetching playlist {p_url}: {e}")

    # ডুপ্লিকেট লিংক বাদ দেওয়া
    unique_urls = list(set([ch.get("url") for ch in all_channels if ch.get("url")]))
    
    health_data = {}
    
    # ThreadPool ব্যবহার করে দ্রুত অনেকগুলো লিংক একসাথে চেক করা
    print(f"Checking {len(unique_urls)} URLs...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_url, unique_urls)
        
        for url, is_working in results:
            if is_working:
                health_data[url] = {"status": "ok"}
            else:
                health_data[url] = {"status": "fail"}
                
    # health.json ফাইলে রেজাল্ট সেভ করা
    with open("health.json", "w") as f:
        json.dump(health_data, f, indent=4)
    print("health.json updated successfully!")

if __name__ == "__main__":
    main()
