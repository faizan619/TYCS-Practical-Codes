import queue as Q
from RMP import dict_gn

start="Arad"
end="Bucharest"
result=" "
def DLS(city,visitedstack,startlim,endlim):
    global result
    found=0
    result=result+city+" "
    visitedstack.append(city)
    if city==end:
        return 1
    if startlim==endlim:
        return 0
    for eachcity in dict_gn[city].keys():
        if eachcity not in visitedstack:
            found=DLS(eachcity,visitedstack,startlim+1,endlim)
        if found:
            return found

def IDDFS(city,visitedstack,endlim):
    global result
    for i in range(0,endlim):
        print("searching at lim:",i)
        found=DLS(city,visitedstack,0,i)
        if found:
            print("found")
            break
        else:
            print("not found")
            print(result)
            result=""
            visitedstack=[]
def main():
     visitedstack=[]
     IDDFS(start,visitedstack,9)
     print("IDDFS traversal from",start,"to",end,"is:")
     print(result)
main()
    
            
        
    
