from sys import set_int_max_str_digits as digits

digits(100_000_000)

# def fib(n, computed = {0: 0, 1: 1}):
# 	if n not in computed:
# 		computed[n] = fib(n-1, computed) + fib(n-2, computed)
# 	return computed[n]
# print(fib(400_000))

def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a+b
	return a
# print(fib(1_000_000))

# требуется подсчитать кол-во послед длинный n сост из 0 и 1 
# в которых никакие две единицы не стоят рядом (по числам фибоначчи)



# codeforces.com -> зарегаться для задачек
# olymp.itas.pstu.ru -> турнир -> спорт. прогр.
# sp.urfu.ru -> квалы на 1/4 финал
# 89197090793
# hawk321@mail.ru