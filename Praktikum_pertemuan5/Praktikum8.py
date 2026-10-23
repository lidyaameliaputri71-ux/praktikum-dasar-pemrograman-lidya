def faktorial(n):  
    if n < 0:
        raise ValueError("Faktorial tidak terdefinisi untuk bilangan negatif") 
    if n <= 1:
        return 1
    return n * faktorial(n - 1)
print(faktorial(5))
try:
    print(faktorial(-3))
except ValueError as e:
    print("Error:", e)