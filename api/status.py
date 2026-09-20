from http.server import BaseHTTPRequestHandler
import json
import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        payload = {
            "status": "online",
            "service": "T37 Wealth Core API",
            "runtime": "Python 3.12 (Vercel Serverless)",
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "version": "1.0.0"
        }
        self.wfile.write(json.dumps(payload, indent=2).encode('utf-8'))
