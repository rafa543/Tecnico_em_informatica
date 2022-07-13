# ano = 2005
# if(ano % 4 == 0 & ano % 100 == 0 & ano % 400 == 0):
#     print("E bissexto")

print(2004 % 100 == 0)

for n in range(2004, 2097, 1):
    if(n % 4 == 0 or n % 100 == 0 or n % 400 == 0):
        print(n, "e bissexto (tem 366)")
    else:
        print(n, "não e bissexto (tem 365 dias)")


# for n in range(2004, 2097, 1):
#     if(n % 4 == 0 & n % 100 == 0 & n % 400 == 0):
#         print(n, "e bissexto (tem 366)")
#     else:
#         print(n, "não e bissexto (tem 365 dias)")
