import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import sys

# --- CONFIGURATION (Yahan koi kharcha nahi!) ---
NUM_BROWSERS = 2  # Sirf 2 browser ek saath chalenge (Free Tier ke liye)
WATCH_DURATION = 300  # 300 seconds = 5 minutes (High Retention ke liye)

# --- Yahan Customer ka Link aayega ---
YOUTUBE_URLS = os.environ.get('YOUTUBE_LINKS', '').split(',')

def setup_driver():
    """Chrome browser setup (Render.com ke liye zaroori)"""
    chrome_options = Options()
    # Yeh headless mode zaroori hai Render.com ke liye
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'])}")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(60)
    return driver

def watch_video(url):
    """Video dekho (High Retention ke liye 5 minute)"""
    if not url.strip():
        return
    
    driver = None
    try:
        driver = setup_driver()
        print(f"Watching: {url} for {WATCH_DURATION} seconds...")
        driver.get(url)
        time.sleep(5)  # Page load hone ka time
        
        # Video play karne ka code (JavaScript se)
        driver.execute_script("document.querySelector('video').play();")
        
        # Ab video dekho 5 minute tak! Yahi Watch Time hai!
        time.sleep(WATCH_DURATION)
        print(f"Finished watching {url}.")
        
    except Exception as e:
        print(f"Error watching {url}: {e}")
    finally:
        if driver:
            driver.quit()

def main():
    if not YOUTUBE_URLS or YOUTUBE_URLS == ['']:
        print("No YouTube URLs provided. Mission aborted.")
        return

    print(f"Starting Mission for {len(YOUTUBE_URLS)} videos...")
    
    # Har URL ko baar-baar dekhenge (jitni baar Render allow kare)
    for _ in range(NUM_BROWSERS):
        for url in YOUTUBE_URLS:
            watch_video(url)
            
    print("Mission complete. Waiting for next cycle.")
    sys.exit(0)

if __name__ == "__main__":
    main()
