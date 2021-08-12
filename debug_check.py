def nextto(arg):

    if arg[arg.index("Arif")+1] or arg[arg.index("Arif")-1] == arg[arg.index("Raife")] :
        return True
    else: False

print(nextto(["Arif","Nihal","Raife"]))
print(nextto(["Arif","Raife","Nihal"]))