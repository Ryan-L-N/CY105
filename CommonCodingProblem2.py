
#Find the left and right index of a target value in a list
def left_right_finder(a_list,target):
    ans_list = []
    for i in range(len(a_list)):
        if a_list[i] == target:
            ans_list.append(i)
            break
    for i in range(len(test)):
        if test[-i] == target:
            ans_list.append(len(a_list)-i)
            break
    if ans_list == []:
        return [-1,-1]
    else:
        return ans_list

test = [0,1,2,3,4,4,4,5,6]  #Expecting 4,6

ans = left_right_finder(test,7)
print(ans)