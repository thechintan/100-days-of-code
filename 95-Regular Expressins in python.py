import re

pattern=r"[A-Z]+ddhava"
text='''In 1800, he was initiated into the Uddhava Bddhava sampradaya by his guru, Swami Ramanand, and was given the name Sahajanand Swami. Despite opposition, in 1802, Ramanand handed over the leadership of the Uddhava Sampradaya to him before his death.[8] According to the Swaminarayan tradition, Sahajanand Swami became known as Swaminarayan, and the Uddhava Sampradaya became known as the Swaminarayan Sampradaya, after a gathering in which he taught the Swaminarayan Mantra to his followers.'''
match=re.search(pattern,text)
print(match,'\n')

matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])