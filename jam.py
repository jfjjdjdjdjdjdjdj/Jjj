import requests
from eth_account import Account

def get_eth_balance(address):
    url = f'https://api.etherscan.io/api'
    params = {
        'module': 'account',
        'action': 'balance',
        'address': address,
        'tag': 'latest',
        'apikey': 'YourApiKeyToken'  # استخدم مفتاح Etherscan الخاص بك
    }
    try:
        r = requests.get(url, params=params)
        result = r.json()
        if result['status'] == '1':
            balance_wei = int(result['result'])
            return balance_wei / 10**18  # تحويل من wei إلى ETH
        else:
            return None
    except:
        return None

def main():
    with open("keys.txt", "r") as f:
        keys = [line.strip() for line in f if line.strip()]

    for priv in keys:
        try:
            acct = Account.from_key(priv)
            address = acct.address
            balance = get_eth_balance(address)
            if balance and balance > 0:
                print(f"[+] {address} → {balance:.6f} ETH")
        except Exception as e:
            print(f"خطأ في المفتاح: {priv[:10]}...")

if __name__ == "__main__":
    main()