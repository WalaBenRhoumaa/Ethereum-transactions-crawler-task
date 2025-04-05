# app.py
from flask import Flask, request, render_template, redirect, url_for
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import time

load_dotenv()
app = Flask(__name__)

ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    transactions = []
    balance = None
    transaction_count = 0
    per_page = 10
    page = int(request.args.get('page', 1))

    if request.method == 'POST':
        address = request.form['address']
        start_block = request.form['start_block']
        date_input = request.form.get('date')
        # Store user input in session or global to preserve on pagination
        app.config['USER_INPUT'] = {
            'address': address,
            'start_block': start_block,
            'date_input': date_input
        }
        return redirect(url_for('index'))

    user_input = app.config.get('USER_INPUT')
    if user_input:
        address = user_input['address']
        start_block = user_input['start_block']
        date_input = user_input['date_input']

        url_eth = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock={start_block}&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_KEY}"
        response_eth = requests.get(url_eth)
        eth_transactions = response_eth.json().get('result', []) if response_eth.status_code == 200 else []

        url_token = f"https://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock={start_block}&endblock=99999999&sort=asc&apikey={ETHERSCAN_API_KEY}"
        response_token = requests.get(url_token)
        token_transactions = response_token.json().get('result', []) if response_token.status_code == 200 else []

        all_transactions = eth_transactions + token_transactions
        all_transactions.sort(key=lambda x: int(x['timeStamp']))
        transaction_count = len(all_transactions)

        start = (page - 1) * per_page
        end = start + per_page
        transactions = all_transactions[start:end]

        if date_input:
            dt = datetime.strptime(date_input, "%Y-%m-%d")
            timestamp = int(time.mktime(dt.timetuple()))
            block_url = f"https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp={timestamp}&closest=before&apikey={ETHERSCAN_API_KEY}"
            block_res = requests.get(block_url).json()
            if block_res['status'] == '1':
                block_number = block_res['result']
                balance_url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag={hex(int(block_number))}&apikey={ETHERSCAN_API_KEY}"
                balance_res = requests.get(balance_url).json()
                if balance_res['status'] == '1':
                    balance = int(balance_res['result']) / 1e18

    total_pages = (transaction_count + per_page - 1) // per_page

    return render_template('index.html', transactions=transactions, balance=balance, transaction_count=transaction_count, page=page, total_pages=total_pages)


if __name__ == '__main__':
    app.run(debug=True)
