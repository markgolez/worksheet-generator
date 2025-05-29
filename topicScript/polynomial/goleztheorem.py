import math
def combi(n , r):
    ''' (numbers, numbers) ->  numbers

    Return the value of n taken r


    >>> combi(3, 2)
    3
    >>> combi(4, 2)
    6
    '''
    ans = math.factorial(n)/((math.factorial(r))*math.factorial(n-r))
    final = int(ans)
    return final

def combi_coef(x):
    '''(sequence of numbers) -> string

    Return the value of the summation of

    '''
    coef = [x[0]]
    com = coef
    total = 0   
    for i in range(len(x) - 1):
        for j in range(i+2):
            total = total + ((-1)**j)*(combi(i + 1, j))*(x[i + 1 - j])
        coef.append(total)
        total = 0
    return com


def stirling(n, r):
    '''(numbers, numbers) -> numbers

    Return the value of stirling numbers

    >>> stirling(4, 3)
    6
    >>> stirling(6, 4)
    85
    '''

    temp = [1, 1]
    for i in range(n-2):
        for j in range(i +3):
            if j == 0:
                b = []
                y = math.factorial(i + 2)
                b.append(y)
            elif j == i + 2:
                y = 1
                b.append(y)
            else :
                y = (temp[j])*(i + 2) + temp[j-1]
                b.append(y)
        temp = b
    
    return temp[r - 1]


def stirling_list(n):
    '''(numbers, numbers) -> numbers

    Return the value of stirling numbers

    >>> stirling(4, 3)
    6
    >>> stirling(6, 4)
    85
    '''
    final_temp = []
    temp = [1, 1]
    for i in range(n-2):
        for j in range(i +3):
            if j == 0:
                b = []
                y = math.factorial(i + 2)
                b.append(y)
            elif j == i + 2:
                y = 1
                b.append(y)
            else :
                y = (temp[j])*(i + 2) + temp[j-1]
                b.append(y)
        temp = b
    
    parity = (len(temp))%2
    if parity == 0:
        for m in range(len(temp)):
            tempo = ((-1)**(m + 1))*(temp[m])
            final_temp.append(tempo)
    else :
        for m in range(len(temp)):
            tempo = ((-1)**(m))*(temp[m])
            final_temp.append(tempo)
       
    return final_temp
    
    
def num_coef(x):
    ''' (list) -> number

    Return the number of nth difference level + 1 of the sequence x
	


    >>> x = [1, 4, 9, 16, 25, 36, 49]
    >>> num_coef(x)
    3
    >>> x = (1, 2, 3, 4, 5, 6)
    >>> num_coef(x)
    2
    '''


    number_list = 0
    coef_list = combi_coef(x)
    for i in range(len(x)):
        if coef_list[len(coef_list) - (len(coef_list) + i + 1)] == 0 :
            number_list = 0
        else :
            number_list = len(coef_list) - i
            return number_list

def polynomial(x):
    ''' (number, number, ...) -> string

    Return the list  ...

    >>> x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    >>> polynomial(x)
    [[1], [3, 3], [4, 6, 2]]

    >>> polynomial(2, 16, 54, 128)
    P(x) = 2x^3
    '''

      
    num_coef_list = num_coef(x)
    variables = []
    list_coefs = combi_coef(x)
    for i in range(num_coef_list):
        y = 'var_' + str(i)
        variables.append(y)
        if i == 0:
            variables[0] = [x[0]]
            temp1 = [x[0]]
        else :
            variables[i] = stirling_list(i + 1)
            for j in range(len(variables[i])):            
                temp = list_coefs[i]*variables[i][j]
                temp1.append(temp)
                
        variables[i] = temp1
        temp1 = []


    for i in range(len(variables)):
        for j in range(i + 1):
            numera = variables[i][j]
            denomi = math.factorial(i)
            frac = str(numera) + '/' + str(denomi)
            variables[i][j] = frac
    
    final = [] 
    for i in range(len(variables)):
        if i != len(variables)-1:
            tempo = variables[i][i]
            a = tempo[ : tempo.rindex('/')]
            b = tempo[tempo.rfind('/') + 1 : ]
            for j in range(len(variables) - (i + 1)):
                temporary = variables[j + i + 1][i]
                c = temporary[ : temporary.rindex('/')]
                d = temporary[temporary.rfind('/') + 1: ]
                e = int(a)
                f = int(b)
                g = int(c)
                h = int(d)
                frac_ans = op_frac(e, f, g, h, '+')
                a = frac_ans[ : frac_ans.rfind('/')]
                b = frac_ans[frac_ans.rfind('/') + 1 :]                
            final.append(frac_ans)
            
        else :
            last = variables[len(variables)-1][len(variables)-1]
            final.append(last)
    ultimate = []
    for i in range(len(final)):
        tempor = final[0 - (i + 1)]
        
        a = tempor[ : tempor.rindex('/')]
        b = tempor[tempor.rfind('/') + 1 : ]
        
        p = int(a)
        q = int(b)
        if (p/q) == (p//q):
            z = int(p/q)
            ultimate.append(z)
        else :
            if p == 0:
                ultimate.append(0)
            elif p == q :
                ultimate.append(1)
            else :
                for j in range(100):
                    while p%(j + 2) == 0 and  q%(j + 2) == 0:
                        p = p/(j + 2)
                        q = q/(j + 2)                      
                fi = str(a) + '/' + str(b)
                ultimate.append(fi)
        
            
    return(ultimate)

def op_frac(a, b, c, d, operation)    :
    '''(numbers, numbers) -> numbers

    Return the answer in fraction form

    >>> op_frac(1, 2, 1, 2, '*')
    1/4
    >>> op_frac(1, 2, 1, 4, '+')
    3/4
    '''
    
    if operation == '*' :
        nu = (a*c)
        de = (b*d)
        
    elif operation == '/' :
         nu = (a*d)
         de = (b*c)
         
    elif operation == '+' :
         de = (b*d)
         nu = (((de/b)*a) + ((de/d)*c))
         
    elif operation == '-' :
         de = (b*d)
         nu = (((de/b)*a) - ((de/d)*c))
    else :
        return 'unrecognized operation'

    for j in range(20):
        while nu%(j + 2) == 0 and  de%(j + 2) == 0:
            nu = (nu/(j + 2))
            de = (de/(j + 2))
    

    nu = int(nu)
    de = int(de)
    nume = str(nu)
    deno = str(de)
    answer = nume + '/' + deno

    return answer


