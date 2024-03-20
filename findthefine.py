class Solution:
    def totalFine(self, n, date, car, fine):
        #Code here
        totalFine=0
        for i in range(n):
            last_digit = car[i] % 10
            if date % 2 ==0: #even date
                if last_digit % 2 != 0: #odd fine
                    totalFine +=fine[i]
            else:    
                if last_digit % 2 == 0:
                    totalFine += fine[i]
        return totalFine            
     