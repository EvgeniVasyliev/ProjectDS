import numpy as np
number = np.random.randint(1, 101) # компьюткр загадал число
print(f'загаданное компьютером число = {number}')
count = 0
left_number = 1 #левая граница
right_number = 101 #правая граница
predict_number = np.random.randint(1, 101) # предполагаемое число
print(f'Предполагаемое число {predict_number}')

while True:
    count += 1
    if number < predict_number:
        right_number = predict_number
        predict_number = int(np.mean(np.arange(left_number, right_number))) + 1
        print(f'попытка {count}, предполагаемое число {predict_number}')
    elif number > predict_number:
        left_number = predict_number
        predict_number = int(np.mean(np.arange(left_number, right_number))) + 1
        
        print(f'попытка {count}, предполагаемое число {predict_number}')
    else:
        print(f'Ваше число {number} угадано за {count} попыток')
        break  # выход из цикла если угадали
#return count   
