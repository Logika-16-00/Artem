with open ("quotes.txt", "r", encoding= "utf-8") as file:
    for line in file:
        print (line)


a = input('а хто написав')
with open ("quotes.txt", "a", encoding= "utf-8") as file:
    file.write("\n "+a+" \n")

while 1:
    b = input('чи хочеш додати')
    if b == "ні":
        break
    else:
        q = input('цитата')
        with open ("quotes.txt", "a", encoding= "utf-8") as file:

            file.write("\n "+q+" \n")
            file.close()
        a = input('а хто написав')
        with open ("quotes.txt", "a", encoding= "utf-8") as file:
            file.write("\n "+a+" \n")

b = input('чи хочеш додати')