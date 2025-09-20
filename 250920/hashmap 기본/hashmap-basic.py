n=int(input())
d={}
for _ in range(n):
    command_line=input().split()
    if command_line[0]=='add':
        d[command_line[1]]=command_line[2]
    else:
        if command_line[0]=='remove':
            d.pop(command_line[1])
        else:
            print(d[command_line[1]] if command_line[1] in d else 'None')
