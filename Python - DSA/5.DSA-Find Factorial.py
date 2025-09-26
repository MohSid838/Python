# def fact(x:int):
#     result=1
#     for x in range(1,x+1):
#         result=x*result
#     return result
# print(fact(5))

# def factor(x:int):
#     if x==1 or x==0:
#         return True
#     fact=1
#     y=1
#     while fact<x:
#         y=y+1
#         fact=fact*y
#     return fact==x
# print(factor(120))
#find new
if __name__ == "__main__":
    x = input("Enter number 1: ")
    y = input("Enter number 2: ")
    try:
        z = x / int(y)

    except Exception as e:
        print("Exception type: ", type(e).__name__)
        print("Exception occurred:", e)
        z = None

    finally:
        print(z)