fd=open("datos txt/mbox.txt","r")


cont=0
for linea in fd:
    if linea.startswith("From:"):
        cont+=1

print(cont)

# cont=0
# fd.seek(0)
# linea = fd.readline()
# while linea:
#     cont+=1
#     linea = fd.readline()

# print(cont)
fd.close()