import argparse
import random

ap = argparse.ArgumentParser(description="The program generates possible usernames and passwords commonly used by people based on their personal details.")
ap.add_argument("-f", "--firstname", required=False,default="", help="First name")
ap.add_argument("-l", "--lastname", required=False,default="", help="Last name")
ap.add_argument("-m", "--middlename", required=False,default="", help="Middle name")
ap.add_argument("-y","--birthyear", required=False,default="", help="Birth year")

args = vars(ap.parse_args())

num_list = [0,1,2,3,4,5,6,7,8,9]
end_num = ["007","77","123","69","12","777","666","420","7","10","11"]

number = '{:03d}'.format(random.randrange (1,999))

fnfl = args["firstname"][0]
lnfl = args["lastname"][0]

print("The details entered are as follows : \n First Name = "+args["firstname"]+"\nLast Name = "+args["lastname"]+"\nBirth Year = "+args["birthyear"])

print("Possible usernames : \n")
for num in num_list:
	print(args["firstname"]+str(num))
	
for endPatt in end_num:
	print(args["firstname"].lower()+endPatt)


