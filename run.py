import os
import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('retry_event.html')


@app.route('/send_event', methods=['POST'])
def retry_event():
    endpoint_url = request.form.get('endpointUrl')
    event_data = request.form.get('eventData')
    r = requests.post(
        endpoint_url,
        headers={
            'Content-Type': 'application/json; charset=utf8',
            'Cache-Control': 'no-cache',
            'User-Agent': 'Stripe/1.0 (+https://stripe.com/docs/webhooks)',
        },
        data=event_data
    )
    return (
        json.dumps({'success': bool(r.status_code == 200)}),
        r.status_code,
        {'Content-Type': 'application/json'}
    )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
