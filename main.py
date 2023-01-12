# Tính giai thừa
def giaiThua():
    n=int(input("Nhập vào số để tính giai thừa : "))
    if n <0:
        exit()
    giaithua=1
    for i in range(1,n+1):
        giaithua*=i
    print(giaithua)
    return 0

giaiThua()