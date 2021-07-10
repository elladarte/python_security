import hashlib

string = 'Phython Security'

resultado_md5 = hashlib.md5(string.encode('utf-8'))
resultado_sha1 = hashlib.sha1(string.encode('utf-8'))
resultado_sha256 = hashlib.sha256(string.encode('utf-8'))

print(f"O hash MD5 da string é: {resultado_md5.hexdigest()}")
print(f"O hash SHA1 da string é: {resultado_sha1.hexdigest()}")
print(f"O hash SHA256 da string é: {resultado_sha256.hexdigest()}")
