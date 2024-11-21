Input_File = open("input1.txt","r")
Data=[]
for lines in Input_File:
    Data.append(lines.rstrip('\n'))

Rod_len=[]
Prices=[]

for x in Data:
    try:
        length = int(x)
        Rod_len.append(length)
    except:
        li=[]
        for value in x[1:-1].split(","):
            price = int(value)
            li.append(price)
        Prices.append(li)

def cut_rod(P,num):
    if num==0:
        return 0
    Max_revenue = -1
    for i in range(0,num):
        total = P[i] + cut_rod(P,num-i-1)
        if total> Max_revenue:
            Max_revenue = total
    return Max_revenue    

for count in range(0,len(Rod_len)):
    print('Maximum Revenue: ',cut_rod(Prices[count],Rod_len[count]))
