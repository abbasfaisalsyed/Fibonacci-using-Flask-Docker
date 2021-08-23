import copy


class Fibonacci_Sum:
    def get_fibonacci_numbers(num):
        
        if (num < 4):
            return None
        fib = []
        n1, n2 = 2, 3
       
        while n1 < num:
            fib.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
          
        return fib

    def calculate_fibonacci_sum_recursively(target, existing_sum, begin, output, buffer, pool):
     if existing_sum == target:
       output.append(copy.copy(buffer))

     for i in range(begin, len(pool)):
       temporary_sum = existing_sum + pool[i]
       if temporary_sum <= target:
         buffer.append(pool[i])
         Fibonacci_Sum.calculate_fibonacci_sum_recursively(target, temporary_sum, i, output, buffer, pool)
         buffer.pop()
       else:
         return

    def calculate(target):
     output = []
     buffer = []
     pool = Fibonacci_Sum.get_fibonacci_numbers(target)
     Fibonacci_Sum.calculate_fibonacci_sum_recursively(target, 0, 0, output, buffer, pool)
     return output
