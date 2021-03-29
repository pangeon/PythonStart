ZWo = 176.0  # wzorst
ot = 86.0  # obwód pasa
obt = 100.0  # obwód bioder

ZTv = 110.0  # wysokość talii
ZUo = 84.0  # wysokość krocza
ZKo = 50.0  # wysokość kolan

# KONSTRUKCJA PRZEDNIEJ CZĘŚCI NOGAWKI
TD = ZTv

TT1 = 3.5

TU = ZTv - ZUo

UB = 1/20 * obt + 3.0

DK = ZKo

DD1 = 2.0

BB1 = 1/4 * obt + 0.0

B1B2 = 1/20 * obt - 0.5

BB2 = BB1 + B1B2

BB3 = 1/2 * BB2

D1D2 = BB3 + 1.5

B1A = 1/4 * UB

AA1 = 0.5

T1T4 = 1/10 * (obt - ot) - 0.5

D3D5 = (1/2 * (1/4 * obt)) - 1

D3D4 = D3D5
K1K2 = D3D4
K1K3 = K1K2
# KONSTRUKCJA PRZEDNIEJ CZĘŚCI NOGAWKI

# KONSTRUKCJA TYLNIEJ CZĘŚCI NOGAWKI
B3B4 = 1.8
B5B7 = 1/4 * obt + 2.0

b = B5B7 + ((1/4 * obt - 6) - B1B2)

B4B6 = 1/2 * b
B4B5 = B4B6

B5B7 = 1/4 * obt + 2.0

T5T6 = 1/20 * obt - 1.5

D5D7 = 2.0
D4D6 = D5D7

K3K5 = 2.0
K2K4 = K3K5

T7T8 = T1T4 + 0.5

T6T8 = 1/4 * obt

T6T9 = 1/2 * T6T8

T4T3 = BB1 - T1T4

t = (T4T3 + T6T8) - (1/2 * ot + 1.5)
# KONSTRUKCJA TYLNIEJ CZĘŚCI NOGAWKI

print(locals())
