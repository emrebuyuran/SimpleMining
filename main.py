from hashlib import sha256
import time

def _SHA256(val):
    return sha256(val.encode()).hexdigest()

def mine(transactions, previous_hash, difficulty):
    prefix_zeros = '0'*difficulty
    nonce = 0
    while True:
        nonce += 1
        val = transactions + previous_hash + str(nonce)
        hash = _SHA256(val)
        if(hash.startswith(prefix_zeros)):
            print(f"Nonce finded : {nonce}")
            return hash

def main():
    difficulty = 6
    transactions = "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
    previous_hash = "0000000000000000000449a35ced446214803e009bca7c2d6f83b36bc71e5ede"
    start_time = time.time()
    print("Mining started...")
    hash = mine(transactions, previous_hash, difficulty)
    total_time = str(time.time() - start_time)
    print(f"Mining completed in {total_time} secs")
    print(f"Hash : {hash}")

main()
