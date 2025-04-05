# Ethereum Wallet Transactions

This project allows users to fetch Ethereum wallet transactions, including ERC-20 token transfers, and check the balance of an address on a specific date using the Etherscan API.

## Requirements

- Python 3.x
- Flask
- Requests
- Python-dotenv

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages by running:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory with the following content:

    ```ini
    ETHERSCAN_API_KEY=your_etherscan_api_key
    ```

    Replace `your_etherscan_api_key` with your actual Etherscan API key.

## Running the Application

To start the Flask application, run:

```bash
python app.py
The app will be accessible at http://127.0.0.1:5000/.

Usage
Enter the Ethereum wallet address and the start block number.

Optionally, specify a date to fetch the balance for that date.

Click "Fetch Transactions" to view the transactions and token transfers.
Pagination: The transactions are displayed with pagination. You can navigate between pages of transactions by clicking the "Next" and "Previous" buttons, or by directly selecting a page number.

License
This project is open-source and available under the MIT License.
## 🎥 Demo Video

Watch a short demo of the Ethereum Transactions Crawler in action:  
[▶️ Click here to watch the video](https://drive.google.com/file/d/1w1D-1MrHjTh96XxiUBK1WlBGm8rde-Jy/view?usp=sharing)
