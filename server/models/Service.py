class Service:
    def __init__(self, name=None):
        self.name = name

    def generate_segitiga(self,number):
        if self.is_number(number) == False:
            return "Input harus berupa angka"
        number_str = str(number)
        length = len(number_str)
        result = []
        for i in range(length):
            line = number_str[i] + '0' * i
            result.append(line)

        result = '\n'.join(result)
        return result
    

    def generate_bilangan_ganjil(self, max):
        if self.is_number(max) == False:
            return "Input harus berupa angka"
        data_number = []

        for num in range(int(max) + 1):
            if num % 2 != 0:
                data_number.append(num)

        result = '\n'.join(map(str, data_number))
        return result
    
    def generate_bilangan_prima(self, max):
        if self.is_number(max) == False:
            return "Input harus berupa angka"
        data_number = []
        max = int(max)
        if max < 2:
            return ""
        
        for num in range(1, max):
            count = 0
            for i in range(num):
                if num % (i+1) == 0:
                    count += 1

            if count == 2:
                data_number.append(num)
        
        result = '\n'.join(map(str, data_number))
        return result
    
    def is_number(self, number):
        try:
            int(number)
            return True
        except ValueError:
            return False
