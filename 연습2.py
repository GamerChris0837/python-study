# 인치 cm 계산기

x=int(input("inch to cm(1)\ncm to inch(2) :"))

if x==1:
    a=float(input("몇인치?"))
    cm=float(a)*2.54
    print("%.2f인치 = %.4fcm"% (a,cm))
elif x==2:
    b=float(input("몇cm?"))
    inch=float(b)/2.54
    print("%.2fcm = %.4f인치"% (b,inch))
else:
    print(">:(")