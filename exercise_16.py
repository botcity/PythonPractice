#!/usr/local/bin/python3.4


##
## Practice Python Course: Exercise 16
## Password Generator
##

import random
import string

symbols = "!@#$%^&*()"
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + symbols
weak_list = ["password", "Password123", "adminpassword", "password123", "thiseasypassword", "newpassword", "oldpassword"]


def strngPwd():
	strong_pwd = ''.join(random.sample(chars, 8))
# 	pwdCheck(strong_pwd)
	print("Your password is: " + strong_pwd)
	
# def pwdCheck(pwd):
# 	char_up = string.ascii_uppercase
# 	char_low = string.ascii.lowercase
# 	char_dig = string.digits
# 	char_sym = symbols
# 	for element in char_up:
# 		if element 
# 	if pwd has acsii.uppercse + acsii_lowercase + ascii.digits + charachter string:
# 		return
# 	if not:
# 		run strgPwd() again
# 	for element in 
	


def weakPwd():
	weak_pwd = random.choice(weak_list)
	print("Your password is: " + str(weak_pwd))


def main():
	question = input("Would you like a strong password or weak password?: ")
	if question == "strong":
		strngPwd()
	elif question == "weak":
		weakPwd()
	else:
		main()
	



if __name__ == "__main__":
	main()
	
exit()