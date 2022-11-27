my_list = [0,1,2,3,4,5,6,7,8,9]

# code nay chay duoc
for x in my_list:
    so_du = x % 2
    if so_du == 0:
        print(f"{x} la so chan")
    else:
        print(f"{x} la so le ")