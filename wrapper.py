import asyncio
import tixte
import os
import json
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Load settings.json
def load_config():
    with open("settings.json", "r") as file:
        return json.load(file)

config = load_config()
UPLOAD_KEY = config["uploadKey"]
DOMAIN = config["domain"]

# Folder to watch
SCREENSHOT_FOLDER = os.path.expanduser("~/Pictures/Screenshots")

class ScreenshotHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        
        if event.src_path.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")):
            print(f"New screenshot detected: {event.src_path}")
            asyncio.run(upload_to_tixte(event.src_path))

async def upload_to_tixte(file_path):
    client = tixte.Client(UPLOAD_KEY, DOMAIN)
    file = tixte.File(file_path)

    async with client:
        try:
            upload = await client.upload(file)
            print(f"Uploaded: {upload.url} ({upload.filename})")

            # Use subprocess to copy the URL to clipboard (more stable)
            subprocess.run(["xclip", "-selection", "clipboard"], input=upload.url.encode(), check=True)
            print(f"URL copied to clipboard: {upload.url}")

        except Exception as e:
            print(f"Upload failed: {e}")

def watch_screenshots():
    event_handler = ScreenshotHandler()
    observer = Observer()
    observer.schedule(event_handler, SCREENSHOT_FOLDER, recursive=False)
    observer.start()
    
    print(f"Watching for new screenshots in {SCREENSHOT_FOLDER}...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    watch_screenshots()