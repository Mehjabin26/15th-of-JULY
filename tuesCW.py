# # # # # # # # # # # # # # # # # # Day1=(input("Enter a day name: "))
# # # # # # # # # # # # # # # # # # def day_type(day1):
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # #     if input=="sunday":
# # # # # # # # # # # # # # # # # #         print("Your typed day is weekend")
# # # # # # # # # # # # # # # # # #     elif input=="saturday":
# # # # # # # # # # # # # # # # # #         print("Your Entered day is Weekend")
# # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # #         print("this is a weekday")
# # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # day_type(Day1)
# # # # # # # # # # # # # # # # # year=int(input("type a YEAR: "))
# # # # # # # # # # # # # # # # # if year%4==0:
# # # # # # # # # # # # # # # # #         print("True")
# # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # #         print("False")
# # # # # # # # # # # # # # # # x=int(input('Enter a number,x= '))
# # # # # # # # # # # # # # # # y=int(input("Enter,y= "))
# # # # # # # # # # # # # # # # z=int(input("Enter,z = "))
# # # # # # # # # # # # # # # # if x>y and x>z:
# # # # # # # # # # # # # # # #     print("x is greater then Y and Z")
# # # # # # # # # # # # # # # # elif y>x and y>z:
# # # # # # # # # # # # # # # #     print("y is greater than x and z")
# # # # # # # # # # # # # # # # elif z>x and z>y:
# # # # # # # # # # # # # # # #     print("z is greater than x and y")
# # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # #     print("There is no single greatest number")
# # # # # # # # # # # # # # # from dis import RETURN_CONST
# # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # hour=int(input("Enter a hour: "))
# # # # # # # # # # # # # # # minute=int(input('Enter a minute: ' ))
# # # # # # # # # # # # # # # def hour_minute(hour,minute):
# # # # # # # # # # # # # # #     if hour>0 and hour<=23 and minute>0 and minute<=59:
# # # # # # # # # # # # # # #         return True
# # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # #         return False
# # # # # # # # # # # # # # # print(hour_minute(hour,minute))
# # # # # # # # # # # # # # h=float(input("Enter Your Height in meters: "))
# # # # # # # # # # # # # # w=float(input("Enter Your Weight in kg: "))
# # # # # # # # # # # # # # BMI=w/(h*h)
# # # # # # # # # # # # # # print("Your BMI is: ", BMI)
# # # # # # # # # # # # # # def BM_Index(BMI):
# # # # # # # # # # # # # #     if BMI<=18.5:
# # # # # # # # # # # # # #         return"Underweight"
# # # # # # # # # # # # # #     elif BMI>=18.5 and BMI<=24.9:
# # # # # # # # # # # # # #         return "Normal Weight"
# # # # # # # # # # # # # #     elif BMI>=25 and BMI<=29.9:
# # # # # # # # # # # # # #         return "Overweight"
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         return"Obese"
# # # # # # # # # # # # # # print(BM_Index(BMI))
# # # # # # # # # # # # # a=int(input("Enter the value of a= "))
# # # # # # # # # # # # # b=int(input("Enter the value of b= "))
# # # # # # # # # # # # # c=int(input("Enter the value of c= "))
# # # # # # # # # # # # # def Find_out(a,b,c):
# # # # # # # # # # # # #     if a==b and b==c and c==a:
# # # # # # # # # # # # #         return "The Triangle is an Equilateral Triangle"
# # # # # # # # # # # # #     elif a==b and a!=c and b!=c:
# # # # # # # # # # # # #         return "The triangle is an Isosceles Triangle"
# # # # # # # # # # # # #     else:
# # # # # # # # # # # # #         return "The Triangle is a Scalene Triangle"
# # # # # # # # # # # # # print(Find_out(a,b,c))
# # # # # # # # # # # # total=int(input("Enter Your Total Purchased Amount: "))
# # # # # # # # # # # # price1=total-(total*(10/100))
# # # # # # # # # # # # price2=total-(total*(5/100))
# # # # # # # # # # # # def final_amount(price1,price2):
# # # # # # # # # # # #     if total>100:
# # # # # # # # # # # #         return price1
# # # # # # # # # # # #     elif total>50:
# # # # # # # # # # # #         return price2
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         return "No Discount is applied"
# # # # # # # # # # # #
# # # # # # # # # # # #
# # # # # # # # # # # # print(final_amount(price1,price2))
# # # # # # # # # # # name=(input("write your name:"))
# # # # # # # # # # # def greet(name1):
# # # # # # # # # # #         print("Hello!",name,"Welcome!")
# # # # # # # # # # # greet(name)
# # # # # # # # # # a=(int(input("Enter a number: ")))
# # # # # # # # # # def check_even_odd(a):
# # # # # # # # # #     if a%2==0:
# # # # # # # # # #         return "the no is even"
# # # # # # # # # #     else:
# # # # # # # # # #         return "the no is odd"
# # # # # # # # # # print(check_even_odd(a))
# # # # # # # # # list=[2,10,1,200]
# # # # # # # # # max=0
# # # # # # # # # def find_largest(max):
# # # # # # # # #     for i in list:
# # # # # # # # #         if i>max:
# # # # # # #             max=i
# # # # # # #              return max
# # # # # # # #  print(find_largest(max))
# # # # # # # # list=[2,4,6,8]
# # # # # # # # def reverse_list(list1):
# # # # # # # #     my_list=[]
# # # # # # # #     for i in range(len(list1)-1,-1,-1):
# # # # # # # #         my_list.append(list1[i])
# # # # # # # #     print(my_list)
# # # # # # # # reverse_list(list)
# # # # # # # vowel=("a","e","i","o","u")
# # # # # # # a=input("write a word: ")
# # # # # # # def count_vowels(vowel):
# # # # # # #     vowel_count=0
# # # # # # #     for i in a:
# # # # # # #         if i in vowel:
# # # # # # #             vowel_count+=1
# # # # # # #     return vowel_count
# # # # # # # print(count_vowels(vowel))
# # # # # # name=input("Enter your name: ")
# # # # # # b=input("mention time(morning/evening/afternoon: ")
# # # # # # def greet_person(a,c):
# # # # # #     if b=="morning":
# # # # # #         return "Good morning:",name
# # # # # #     elif b=="evening":
# # # # # #         return "Good evening: ",name
# # # # # #     elif b=="afternoon":
# # # # # #         return "Good afternoon:",name
# # # # # #     else:
# # # # # #         return"Have a nice day"
# # # # # # print(greet_person(name,b))
# # # # # score=int(input("Enter your score: "))
# # # # # def calculate_grade():
# # # # #     for i in range(0,100):
# # # # #         if score>=90 and score<=100:
# # # # #             return "Your Score is A"
# # # # #         elif score>=80 and score<=89:
# # # # #             return "Your Grade is B"
# # # # #         elif score>=70 and score<=79:
# # # # #             return "Your score is C"
# # # # #         elif score>=60 and score<=69:
# # # # #             return "Your Grade is D"
# # # # #         else:
# # # # #             return "Your Grade is F"
# # # # #
# # # # # print(calculate_grade())
# # # # num=int(input("Enter a number: "))
# # # # def is_positive(num1):
# # # #     if num>=0:
# # # #         return "True"
# # # #     else:
# # # #         return"False"
# # # # print(is_positive(num))
# # # list=[1,2,3,4,5,6,7,8]
# # # def filter_even(list1):
# # #     new_list=[]
# # #     for i in range(len(list)):
# # #         if i%2!=0:
# # #             new_list.append(list1[i])
# # #     print(new_list)
# # # (filter_even(list))
# # list=[0,1,2,3,4,5,6,7,8,9,10]
# # def sum_list(list1):
# #     total=sum(list)
# #     return total
# #
# # print(sum_list(list))
# list_A=[5,6,7,7,8,5,9,2,1,3,3]
# def remove_duplicates(list1):
#     list1=list(dict.fromkeys(list1))
#     return list1
#
# print(remove_duplicates(list_A))
contact_info={}
phn_no="contact_info"":""{""123-456-7890""}"
def add_phn_no(contact_info,phn_no):
    contact_info=phn_no
    for i in range(phn_no):
        contact_info.append(i)
        return phn_no
print(phn_no)
