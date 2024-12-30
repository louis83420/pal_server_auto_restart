import os
import psutil
import time
import schedule

# 定義應用程式名稱與路徑
APP_NAME = "PalServer-Win64-Shipping-Cmd.exe"
APP_PATH = r"D:\steamcmd\steamapps\common\PalServer\PalServer-Win64-Shipping-Cmd.exe"

def is_app_running(app_name):
    """檢查應用程式是否運行中"""
    for process in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in process.info['name'].lower():
            return process.info['pid']
    return None

def stop_app(pid):
    """關閉應用程式"""
    try:
        os.kill(pid, 9)  # 強制結束應用程式
        print(f"應用程式已關閉 (PID: {pid})")
    except Exception as e:
        print(f"關閉應用程式時出現錯誤: {e}")

def start_app():
    """啟動應用程式"""
    try:
        os.startfile(APP_PATH)  # 啟動應用程式
        print("應用程式已重新啟動")
    except Exception as e:
        print(f"啟動應用程式時出現錯誤: {e}")

def restart_app():
    """檢查並重啟應用程式"""
    pid = is_app_running(APP_NAME)
    if pid:
        print(f"檢測到應用程式運行中 (PID: {pid})，準備關閉...")
        stop_app(pid)
    else:
        print("未檢測到應用程式運行，準備啟動...")
    start_app()

# 每日 23:59 執行重啟
schedule.every().day.at("23:59").do(restart_app)

print("定時任務已啟動...")
while True:
    schedule.run_pending()
    time.sleep(1)
