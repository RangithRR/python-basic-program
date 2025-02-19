english=int(input("enter your english mark :"))
tamil=int(input("enter your tamil mark :"))
science=int(input("enter your science mark :"))
social=int(input("enter your social mark :"))
maths=int(input("enter your maths mark :"))
total=(english+tamil+science+social+maths)/5
if (total<35):
    print("additional classs requried")
else:
    print("you are ood rank")
