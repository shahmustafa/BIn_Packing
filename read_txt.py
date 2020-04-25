#import nessecary packages if codes shows error

def convert(list):
    # Converting integer list to string list
    # and joining the list using join()
    res = int("".join(map(str, list)))

    return res

def read_txt():
    a = open("Dev.txt", "r")
    for line in a:
        if 'Device Number' in line:
            numDescriptors = line.split(':')
            print('Device Number:',int(numDescriptors[1]))
        if 'Application Number' in line:
            numApplications = line.split(':')
            print('Application Number',int(numApplications[1]))
        if 'Device weights' in line:
            weights = line.split()
            #int_list = [int(a) for a in weights[2]]
            weights = weights[2]
            numbers = []
            for words in weights:
                if words.isdigit():
                    numbers.append(int(words))
            weights = numbers

            print('Device weights:',weights)
            '''
            elem in weights
            if weights[2]:
                numbers = []
                for words in weights[2]:
                    if words.isdigit():
                        numbers.append(int(words))
                weights = numbers

            else:
                randomlist = []
                for i in range(0, 2):
                    n = random.randint(1, 3)
                    randomlist.append(n)
                    weights = randomlist
                    numbers = []
                    for words in weights:
                        if words.isdigit():
                            numbers.append(int(words))
                    weights = numbers
            print(weights)
            '''
        if 'Time constraint' in line:
            timeApplication = line.split()
            numbers = []
            for words in timeApplication[13]:
                for elem in words:
                    #print(elem)
                    if elem.isdigit():
                        numbers.append(int(elem))
            h = convert(numbers)
            print('Hour:', h)
            h = h * 3600

            numbers = []
            for words in timeApplication[14]:
                for elem in words:
                    #print(elem)
                    if elem.isdigit():
                        numbers.append(int(elem))
            m = convert(numbers)
            print('Minutes:',m)
            m = m * 60


            numbers = []
            for words in timeApplication[15]:
                for elem in words:
                    #print(elem)
                    if elem.isnumeric():
                        #elem = (elem.split('.'))
                        numbers.append(int(elem))
            digits = len(numbers) - 2
            s = convert(numbers)
            divide = '1'
            divide = divide.ljust(digits + len(divide), '0')
            divide = int(divide)
            s = s / divide
            print('seconds:',s)
            #s = s/ 1*
            #print(s)
            #print((timeApplication[13],timeApplication[14],timeApplication[15]))
            timeApplication = h + m + s
            print('Time Constraints in Seconds:',timeApplication)

    '''
    b = a.readlines()
    a.close()
    
    count = 0
    for line in b:
        count += 1
        if count==1:
            numDescriptors = line[15:]
            print(numDescriptors)
    
    mylines = []
    with open('dev_test.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
        print(myfile.readlines(50))
        
        for line in myfile:  # For each line of text,
            mylines.append(line)  # add that line to the list.
        for element in mylines:  # For each element in the list,
            #if element == 'Device Number: 100':
            print(element[15:18])
        '''


read_txt()
