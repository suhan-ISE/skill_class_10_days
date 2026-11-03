import re 

text = "please conatct admin@pes.edu.in or info@pes.ac.in or suhankhan.kas@gmail.com"

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
pattern_1 = r'[a-zA-Z0-9._%+-]+@gmail\.[a-zA-Z]{2,}'
emails = re.findall(pattern,text)
gmail = re.findall(pattern_1,text)

print(emails)
print(gmail)