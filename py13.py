def silce_with_step(mylist,start,step):
    result=mylist[start::step]
    return result
input_str=input("请输入一个数列，元素之间用逗号隔开")
try:
    input_list=[int(num.strip())for num in input_str.split(',')]
    start=int(input("请输入切片起始索引："))
    step=int(input("请输入切片步长："))
    result=silce_with_step(input_list,start,step)
    print("切片结果是：",result)
except ValueError:
    print("输入有误")