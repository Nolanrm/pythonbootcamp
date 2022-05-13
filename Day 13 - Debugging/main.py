test = 1

print(test)


print("hello world")

def mutatute(a_list):
    b_list=[]
    for item in a_list:
        new_item = item*2
        b_list.append(new_item)
    print(b_list)

mutatute([1,2,3,5,8,13])