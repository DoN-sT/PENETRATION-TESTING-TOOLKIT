import hashlib
import os



def generate_hash(file_path, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def check_integrity(file_path, original_hash, algorithm='sha256'):
    current_hash = generate_hash(file_path, algorithm)
    return current_hash == original_hash

def main():
    print("*"*50)
    print("1.genarate the hash file ")
    print("2.check the file intigrity")
    print("*"*50)
    op=int(input("Enter option '1' or '2' : "))

    if op==1:
        filepath1=input('enter the file path:')
        fec=os.path.isfile(filepath1)
        if fec:
            hash1=generate_hash(filepath1)
            print("the hash value is :","\n",hash1)
        else:
            print('file not exists!!')
    elif op==2:
        filepath1=input('enter the file path:')
        original_hash=input('enter the original hash:')
        fec=os.path.isfile(filepath1)
        if fec:
            hash2=check_integrity(filepath1,original_hash,)
            if hash2:
                print("*"*70)
                print("the file is safe and original")
                print("*"*70)
            else:
                print('the given file is not original and not safe')
        else:
            print('file not exists!!')

if __name__ == "__main__":
    domain = input("Enter the domain name of the web application (e.g., example.com): ")
    main()
