while True:
	password = input('請輸入密碼:')
	if password == 'a123456789':
		print('恭喜你成功登入!!')
		break
	else:
		print('密碼錯誤，你還有兩次機會!')
		input('請輸入密碼:')
		if password == 'a123456789':
			print('恭喜你成功登入')
			break
		else:
			print('密碼錯誤，你還有一次機會!')
			input('請輸入密碼:')
			if password == 'a123456789':
				print('恭喜你成功登入')
			else:
				print('沒有機會了')
				break
