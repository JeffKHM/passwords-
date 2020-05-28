passwords = '38972929'
还有 = 3 # 剩下三次机会
while 还有 > 0:
	pwd = input('请输入密码：')
	if pwd == passwords:
		print('成功！')
		break 
	else:
		还有 = 还有 - 1
		print('密码错误! 剩下', 还有 , '次机会')
	
            
           
		     
			
		