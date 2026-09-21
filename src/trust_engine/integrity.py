import hashlib


def calculate_hash(data):
    data_bytes = data.encode("utf-8")
    hash_value = hashlib.sha256(data_bytes)

    return hash_value.hexdigest()


def main():
    transaction = "Pay $75,000 to Account A"

    transaction_hash = calculate_hash(transaction)

    print("Transaction:")
    print(transaction)

    print("\nSHA-256 Hash:")
    print(transaction_hash)


if __name__ == "__main__":
    main()
