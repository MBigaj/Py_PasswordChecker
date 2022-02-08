# Checks if your password has ever been hacked
import sys
import requests
import hashlib

def request_api_data(query_char):
	# Hashing a password!!! VERY IMPORTANT - SHA1 Hash (idempotent)
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
	return res

def get_passwd_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	print(response)
	return get_passwd_leaks_count(response, tail)

def main(args):
	for password in args:
		count = pwned_api_check(password)
		if count:
			print(f'{password} was found {count} times... you should consider changing your password')
		else:
			print(f'{password} was NOT found, SAFE TO USE!')
	return 'done!'


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
