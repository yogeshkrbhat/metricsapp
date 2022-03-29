from app import app
from prometheus_client import  Summary
import time


REQUEST_TIME = Summary('testapp_metrics_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()
def home():
   time.sleep(5)
   return "hello metrics world!"

