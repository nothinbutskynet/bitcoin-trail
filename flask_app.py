from flask import Flask, render_template
import logging
import sys

# Set up logging to both file and console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    logger.info("Home page requested")
    return render_template('index.html')

if __name__ == '__main__':
    port = 8080  # Try a different port
    logger.info(f"Starting Flask server on port {port}...")
    print(f"Server starting on http://localhost:{port}")
    print(f"Try also: http://127.0.0.1:{port}")
    print(f"Or: http://0.0.0.0:{port}")
    
    # Run on all interfaces
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True,
        use_reloader=True
    )