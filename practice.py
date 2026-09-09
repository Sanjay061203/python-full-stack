'''
n_t = int(input("enter value: "))
for i in range(n_t):
    w = float(input("enter the weight in kgs: "))
    h = float(input("enter the height in meters: "))
    name = input("enter name: ")
    if w>0 and h>0:
        BMI=w/(h**2)
        print(BMI)
        if (BMI)<18.5:
            print("underweight")
        elif (18.5<=BMI<=24.9):
            print("normal weight")
        elif (25<=BMI<=29.9):
            print("overweight")
        else:
            print("obesity")
    else:
        print("enter correct +ve values")
'''

while true:
    w = float(input("enter weight in kgs: "))
    h = float(input("enter height in metres: "))
    name = input("enter your name: ")
    try:
        if w>0 and h>0:
            break
        
        BMI=w/(h**2)
        print(BMI)
        if (BMI)<18.5:
            print("underweight")
        elif (18.5<=BMI<=24.9):
            print("normal weight")
        elif (25<=BMI<=29.9):
            print("overweight")
        else:
            print("obesity")

    except Exception as e:
        print(f'the error is {e}')
        
    
            
