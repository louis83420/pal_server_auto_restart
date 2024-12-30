Pal Server Auto Restart(幻獸帕魯自薦伺服器重啟)

簡介

Pal Server Auto Restart 是一個使用 Python 撰寫的簡單自動化腳本，用於每天在指定時間檢查並重啟 Pal Server 應用程式。該腳本能夠自動檢測應用程式是否運行，並根據情況執行關閉和重新啟動操作，確保伺服器穩定運行。

功能

自動檢測 Pal Server 是否正在運行。

如果應用程式已運行，會先關閉後再重新啟動。

如果應用程式未運行，則直接啟動。

定時每日 23:59 自動執行檢查和重啟。

系統需求

操作系統: Windows

Python 版本: 3.6 或更高版本

必要模組:

psutil

schedule

安裝與使用

1. 安裝 Python 與必要模組

安裝 Python 並確保已添加至系統環境變數。

安裝必要模組：

pip install psutil schedule

2. 編輯腳本

將 APP_NAME 和 APP_PATH 替換為您的應用程式名稱與完整路徑。

APP_NAME = "PalServer-Win64-Shipping-Cmd.exe"
APP_PATH = r"D:\steamcmd\steamapps\common\PalServer\PalServer-Win64-Shipping-Cmd.exe"

3. 執行腳本

將此腳本儲存為 pal_server_auto_restart.py。

在命令提示字元中切換到腳本所在目錄並執行：

python pal_server_auto_restart.py

4. 背景執行（可選）

若需要將腳本設置為背景執行，您可以使用以下方式：

Windows: 使用 Task Scheduler 設置開機自動執行。

Linux: 使用 nohup 或設定 crontab 自動執行。

原理

使用 psutil 模組檢查指定應用程式是否正在運行。

如果應用程式正在運行，則先關閉。

使用 os.startfile 啟動應用程式。

使用 schedule 模組在每日 23:59 執行上述步驟。

範例輸出

定時任務已啟動...
檢測到應用程式運行中 (PID: 12345)，準備關閉...
應用程式已關閉 (PID: 12345)
應用程式已重新啟動

注意事項

確保 APP_PATH 的路徑正確，並且該應用程式有足夠的權限被啟動。

如果應用程式需要其他環境變數或依賴項，請提前配置好。
