
import re
abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com,aswin@gmail.com,a@gmail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
for email in emails:
    print (email)
