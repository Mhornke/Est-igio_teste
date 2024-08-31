num = 8
anterior = []
fibonacci =[]

for i in range(2):
    num -=1
    anterior.append(int(num))
    
soma = anterior[0]+anterior[1] 
   
num = 0
num2 = 0
while True:
    num = num + num2
    num2 = num - num2
    if num2 == 0:
        num2 = 1
    
    fibonacci.append(num)
    if num2 == 10:
        break 
    
    if len(fibonacci) == 10:
        break      

print(f"{anterior} = " , end="")    
print(soma)

if soma in fibonacci:
    print("Este ºN pertence a sequencia Fibonacci!!")

print(fibonacci)  
  
