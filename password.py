passwords = '38972929'
还有 = 3 # 剩下三次机会
while 还有 > 0:
	还有 = 还有 - 1
	pwd = input('请输入密码：')
	if pwd == passwords:
		print('成功！')
		break 
	else:
		print('密码错误!')
		if 还有 > 0:
			print('还有' , 还有 , '次机会')
		else:
			print('没有机会尝试了！要锁账号了呀！')
	
            
           
		     
			
		