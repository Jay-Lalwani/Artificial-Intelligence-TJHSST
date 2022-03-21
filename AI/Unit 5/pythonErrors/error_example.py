1var = 'bob' #variable name error

test = 'bob'
_test = 'bob'
testing = "1var"
testing2 = '1var'

a, b, 2234 = 'bob' #variable name error

def   function ( )  :
    return

def function2():
    return

function()
print(function2())
function3() #calling undefined function error
print(function5(a, b)) #calling undefined function error

def function6(test1, test2):
    return


function6(a, b)
function6(test1=a, test2=b)
function6() #calling function with wrong number of args
function6(a, b, test) #calling function with wrong number of args

if 5 == 5:
    while 5==4:
        break
elif 'bob' = 5: # = instead of ==
    while 'bob' = 4: # = instead of ==
        break

x = 5
x==5 # == instead of =
x=='bob' # == instead of =
