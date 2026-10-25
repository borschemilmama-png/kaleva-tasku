import os
import threading
import http.server
import socketserver
import time
from playwright.sync_api import sync_playwright

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='dist', **kwargs)
    def log_message(self, format, *args):
        pass

def main():
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    os.makedirs('screenshots', exist_ok=True)

    server = socketserver.TCPServer(('127.0.0.1', 8998), QuietHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server running on port 8998")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path=chrome_path)
            # Mobile viewport to capture the phone screen crisply
            page_mobile = browser.new_page(viewport={'width': 440, 'height': 880})
            page_mobile.goto('http://127.0.0.1:8998')
            page_mobile.wait_for_timeout(1000)
            page_mobile.screenshot(path='screenshots/mobile_card_1.png')

            # Click next story
            next_btn = page_mobile.query_selector('button[aria-label="Seuraava uutinen"]')
            if next_btn:
                next_btn.click()
                page_mobile.wait_for_timeout(600)
                page_mobile.screenshot(path='screenshots/mobile_card_2.png')

            # Desktop viewport to capture full interactive desktop layout
            page_desktop = browser.new_page(viewport={'width': 1400, 'height': 900})
            page_desktop.goto('http://127.0.0.1:8998')
            page_desktop.wait_for_timeout(1000)
            page_desktop.screenshot(path='screenshots/desktop_overview.png')

            # Open broadsheet
            headline_btn = page_desktop.query_selector('button:has-text("LUE KOKO ARTIKKELI")')
            if not headline_btn:
                headline_btn = page_desktop.query_selector('h2')
            if headline_btn:
                headline_btn.click()
                page_desktop.wait_for_timeout(700)
                page_desktop.screenshot(path='screenshots/broadsheet_view.png')

            browser.close()
            print("Screenshots captured successfully!")
    finally:
        server.shutdown()

if __name__ == '__main__':
    main()
