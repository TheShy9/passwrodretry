password = 'a123456'
x = 3
while x > 0:	
	password_test = input('请输入密码: ')
	if password_test == password:
		print('登入成功')
		break
	else:
		x = x - 1
		print('登入失败!还有', x, '次机会')
		

