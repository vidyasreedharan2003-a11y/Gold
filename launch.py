import subprocess, time
from pyngrok import ngrok, conf

conf.get_default().auth_token = "3B77tfrY2f5jE6maku9OXBVP35Q_4uCBGMYdfA2jP8P9CCFMP"

proc = subprocess.Popen(["streamlit","run","app.py","--server.port","8501","--server.headless","true"])
print("Streamlit starting...")
time.sleep(5)

url = ngrok.connect(8501)
print("Public URL:", url)

try:
    proc.wait()
except KeyboardInterrupt:
    ngrok.kill()
    proc.terminate()