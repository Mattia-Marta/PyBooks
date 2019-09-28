'''
Versione 1.0 di "isPhoneNumber: un sacco di cicli e controlli; funzionale ma
poco efficiente. Con analisi di chunk, possiamo cerare all'interno
di un testo di varia dimensione.
'''

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

print('\nQui si inizia a far scorrere il testo:')
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print(message+'\n')
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):         
        print('Phone number found: ' + chunk)
print('Done')