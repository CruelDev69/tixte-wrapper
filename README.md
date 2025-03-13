# Tixte Wrapper

**Tixte Wrapper** is an automated tool that detects new screenshots and uploads them to [Tixte](https://tixte.com) instantly. Developed by **Ahad**.   

## Features  
- **Automatic Upload** – Monitors the screenshot folder and uploads images instantly.  
- **Clipboard Copy** – Copies the uploaded image URL to the clipboard for easy sharing.  
- **Autostart on Login** – Runs automatically when you start your system.  

## Installation  

### Prerequisites  
- Python 3 installed on your system  
- **xclip** for clipboard support (Linux users):  
  ```bash
  sudo apt install xclip
  ```

### Setup  

1. Clone the repository:  
   ```bash
   git clone https://github.com/CruelDev69/tixte-wrapper.git
   cd tixte-uploader
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Configure settings:  
   Edit `settings.json` and add your **uploadKey** and **domain**.  

4. Start the script:  
   ```bash
   python3 wrapper.py
   ```

## Enable Autostart on Login  

1. Open a terminal and run:  
   ```bash
   nano ~/.config/autostart/tixte-uploader.desktop
   ```

2. Add the following lines:  
   ```
   [Desktop Entry]
   Type=Application
   Name=Tixte Wrapper
   Exec=sh -c "cd /home/yourusername/tixte-uploader && python3 wrapper.py"
   Hidden=false
   NoDisplay=false
   X-GNOME-Autostart-enabled=true
   ```

3. Save and exit (`CTRL + X`, then `Y`, then `Enter`).  

## Notes  
- **Ensure `settings.json` is correctly configured before running.**  
- **Do not claim this script as your own.**  

## Contact  
- **Discord:** Ahad#3257  
- **Website:** [itscruel.cf](https://www.itscruel.cf)  

If you find this tool useful, consider giving the repository a ⭐! 