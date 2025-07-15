# def calculation(a,b):
#     add=a+b
#     sub=a-b
#     print("Addition of two numbers",add)
#     print("Subtruction of two numbers",sub)
#     return(add,sub)
# x=int(input('enter a number: '))
# y=int(input('enter another number: '))
#
# calculation(x,y)
#def hello_python():
    #user_input=int(input("Enter a numer: "))
    #for i in range(user_input):
         #print("hello Python")
#hello_python()
#i=0
#while i<=x:
 #   i=i+1
  #  print("hello python")
list=[2,3,5,6]
element=int(input("enter a number: "))
def demo(list1,el):
    if el in list1:
        print("This element exists in the list")
    else:
        list1.append(el)
        print(list1)
demo(list,element)



