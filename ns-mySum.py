def mySum(num):
    #定义总和
    running_sum=0
    #起始值为0
    for i in range(1,num+1):
        #每次循环将i加到总和上(从1开始加，每次加1）
        running_sum+=1
    return running_sum
   
def average3(numList):
    return sum(numList)/len(numList)
