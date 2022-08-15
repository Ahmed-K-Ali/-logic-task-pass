s = 'ahmed12345'
print(s.replace('a', ''))


s = 'ahmed12345'
print(s.translate({ord('a'): None}))


s = 'ahmed12345'
print(s.translate({ord(i): None for i in 'ahmed'}))