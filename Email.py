
import re
abc = input()
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
if(len(email)==0):
    print(0)
else:
    for email in emails:
        print (email)
