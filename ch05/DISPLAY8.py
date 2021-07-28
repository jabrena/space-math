G = int(input("G= "))
n_e = int(input("n= "))
a = []
for i in range(n_e):
    cur = int(input("a" + str(i) + "= "))
    a.append(cur)
S = int(input("S= "))
intrest = float(input("i= "))/100

a_sum_with_i = 0
for i in range(1, n_e + 1):
    a_sum_with_i += a[i-1]/((1+intrest)**i)

KV = -G + a_sum_with_i + S/(intrest+1)**n_e
annu = KV * (intrest)/(1-(intrest+1)**(-n_e))
Pb_1 = 0
sum_1 = 0
Pb_2 = 0
sum_2 = 0
for i in range(n_e):
    if sum_1 + a[i] > G:
        Pb_1 += (G-sum_1)/a[i]
        break
    sum_1 += a[i]
    Pb_1 += 1
for i in range(n_e):
    cur_a = a[i]/(1+intrest)**(i+1)
    if sum_2 + cur_a > G:
        Pb_2 += (G-sum_2)/(cur_a)
        break
    sum_2 += cur_a
    Pb_2 += 1

print("KV: " + str(KV))
print("annu: " + str(annu))
print("PB_1: " + str(Pb_1), "PB_2: " + str(Pb_2) )