#密碼登入程式
#密碼 = a123456
#讓使用者重複輸入密碼(迴圈)
#只有三次輸入機會
#密碼正確就print 登入成功。 密碼錯誤就print 登入失敗，還有__機會

password = 'a123456'
x = 3
while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		if x > 0:
			print('密碼錯誤,還有',x,'次機會')
		x = x - 1
		if x < 0:
			print('已無嘗試機會')
			break

		

