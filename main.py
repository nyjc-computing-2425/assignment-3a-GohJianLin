nric = input('Enter an NRIC number: ')
# Type your code below
nric = nric.upper()
A = nric[0] in "TFGS"
B = nric[1:8].isdecimal()
C = len(nric[8:]) == 1 and nric[8:].isalpha()

digit = 0

if A and B and C:
  digit += int(nric[1])*2
  digit += int(nric[2])*7
  digit += int(nric[3])*6
  digit += int(nric[4])*5
  digit += int(nric[5])*4
  digit += int(nric[6])*3
  digit += int(nric[7])*2

if nric[0] in "TG" :
  digit += 4
rem = digit % 11
S_T = "JZIHGFEDCBA"
F_G = "XWUTRQPNMLK"
if nric[0] in "ST":
  lett = S_T[rem]
elif nric[0] in "FG":
  lett = F_G[rem]
else: 
  lett ="0"
if A and B and C and (nric[8] in lett):
  print('NRIC is valid.')
else:
  print('NRIC is invalid.')