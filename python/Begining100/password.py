def check_len(pwd): 
	if len(pwd)>=8:
		return True
	else:
		return False

def check(pwd):
	check =[0,0,0,0]
	for char in pwd:
		if char.islower():
			check[0]=1
		if char.isupper():
			check[1]=1
		if char.isdigit():
			check[2]=1
		if not (char.isapha()|char.isdigit()|char.isspace()):
			check[3]=1
	if sum(check)==4:
		return True
	else:
		return False

def check_rep(pwd):
	n = len(pwd)
	for i in range(n-4):
		str1 = pwd[i: i+4]
		str2 = pwd[i+4::]
		if str1 in str2:
			return False
	return True

if __name__ == '__main__':
	msg = ''
	while True:
		pwd = input('Please type ur pwd')
		if pwd == 'q':
			print('Bye~')
			break
		
		vcheck1 = check_len(pwd)
		if not vcheck1:
			print('Too short!')
			continue
		
		vcheck2 = check(pwd)
		if not vcheck2:
			print('Not enough!')
			continue

		vcheck3 = check_rep(pwd)
		if not vcheck3:
			print('No double!')
			continue

		print('Welcome!')
		break
