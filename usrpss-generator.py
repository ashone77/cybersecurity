import argparse

ap = argparse.ArgumentParser(description="The program generates possible usernames and passwords commonly used by people based on their personal details.")
ap.add_argument("-f", "--firstname", required=False,default="", help="First name")
ap.add_argument("-l", "--lastname", required=False,default="", help="Last name")
ap.add_argument("-y","--birthyear", required=False,default="", help="Birth year")

args = vars(ap.parse_args())


print("The details entered are as follows : \n First Name = "+args["firstname"]+"\nLast Name = "+args["lastname"]+"\nBirth Year = "+args["birthyear"])

