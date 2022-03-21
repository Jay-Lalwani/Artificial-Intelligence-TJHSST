import re
import sys
vowels = {'a', 'e', 'i', 'o', 'u'}
 
builtInFunctions = '''abs()	enumerate()	iter()	reversed()
all()	eval()	len()	round()
any()	exec()	list()	set()
ascii()	filter()	locals()	setattr()
bin()	float()	map()	slice()
bool()	format()	max()	sorted()
breakpoint()	frozenset()	memoryview()	staticmethod()
bytearray()	getattr()	min()	str()
bytes()	globals()	next()	sum()
callable()	hasattr()	object()	super()
chr()	hash()	oct()	tuple()
classmethod()	help()	open()	type()
compile()	hex()	ord()	vars()
complex()	id()	pow()	zip()
delattr()	input()	print()	__import__()
dict()	int()	property()	
dir()	isinstance()	range()	
divmod()	issubclass()	repr() read() split() exit() lower() count() append() add() remove() isalpha()'''
inp = sys.argv[1]
file = open(inp)
allLines = file.read()
lines = allLines.split('\n')
for index, line in enumerate(lines):
    if '#' in line:
        lines[index] = line[:line.find('#')]

# A variable in python can contain any word character, [A-Za-z0-9_], but can’t begin with a digit. Find variable
# names that begin with digits. (Even cooler if you can exclude results between " or ' marks, to ignore strings.
# That doesn’t have to be done using regex, though it can be.)
varErrors = []
for i, line in enumerate(lines):
    index = i + 1
    exp = re.compile(r"^(\s*|.+\s+)[0-9][A-Za-z0-9_]*\s*(?!==)=\s*.*$")

    for result in exp.finditer(line):
        varErrors.append(index)
print("Checking for variable name errors:")
print("Line Numbers:", varErrors)


# • Any variable in python followed by any number of spaces (including zero) and then an opening parenthesis can
# be assumed to be a function call or a function definition. Find any function calls to undefined functions.
functionDefs = set()
for i, line in enumerate(lines):
    index = i + 1
    exp = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*(?=\s*\(.*\)\s*:)")

    for result in exp.finditer(line):
        functionDefs.add("".join(result[0].split()))


functionCallErrors = []
for i, line in enumerate(lines):
    index = i + 1
    exp = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*(?=\s*\(.*\)(?!\s*:))")

    for result in exp.finditer(line):
        builtIn = False
        try:
            builtIn = callable(eval(result[0]))
        except:
            None
        if builtIn == False:
            builtIn = "".join(result[0].split()) in builtInFunctions
        if "".join(result[0].split()) not in functionDefs and builtIn == False:
            functionCallErrors.append(index)
print()
print("Checking for function call errors:")
print("Line Numbers:", functionCallErrors)

# • Find any function calls to defined functions that have the wrong number of arguments.

functionWithArgs = set()
for i, line in enumerate(lines):
    index = i + 1
    exp = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\s*\(.*\)\s*:")

    for result in exp.finditer(line):
        functionWithArgs.add(result[0])
funcArgsDic = {}
for function in functionWithArgs:
    f = "".join(function.split())[:-1]
    if '()' in f:
        funcArgsDic[f[:f.find('(')]] = 0
    else:
        funcArgsDic[f[:f.find('(')]] = len(f.split(','))

functionArgsErrors = []
for i, line in enumerate(lines):
    index = i + 1
    exp = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\s*\(.*\)(?!\s*:)")

    for result in exp.finditer(line):
        builtIn = False
        tempFunc = "".join(result[0].split())
        if '()' in tempFunc:
            args = 0
        else: args = len(tempFunc.split(','))
        tempFunc = tempFunc[:tempFunc.find('(')]

        try:
            builtIn = callable(eval(tempFunc))
        except:
            None
        
        if builtIn == False and tempFunc in funcArgsDic and args != funcArgsDic[tempFunc]:
            functionArgsErrors.append(index)
print()
print("Checking for function call with incorrent number of arguments:")
print("Line Numbers:", functionArgsErrors)
# • Find situations where = has been used instead of ==. (Again, assume Foundations-level work; no need to go
# down too many rabbit holes for surprising uses. Consider if, elif, while, and return statements, and perhaps
# assigning Boolean values to variables like x = y == 3, which will set x to True or False based on the value of y.)
oneEqualErrors = []
for i, line in enumerate(lines):

    index = i + 1
    exp = re.compile(r"(if|elif|while|return)(?!.*==)(?=.*=)")
    for result in exp.finditer(line):
        oneEqualErrors.append(index)
print()
print("Checking for = instead of == errors:")
print("Line Numbers:", oneEqualErrors)
# • Find situations where == has been used instead of =.
twoEqualErrors = []
for i, line in enumerate(lines):

    index = i + 1
    exp = re.compile(r"^(?!.*(if|elif|while|return).*==)(?=.*==)")
    for result in exp.finditer(line):
        twoEqualErrors.append(index)
print()
print("Checking for == instead of = errors:")
print("Line Numbers:", twoEqualErrors)
# • Find situations where a method is called on a variable before that variable has been defined. (ie, a.append(3)
# before any line that says a = something, or a function definition where a is passed as an argument.)

# • Find a situation where a student who is used to coding in Java maybe wrote some Java code in Python by
# mistake. Be specific about the situation you’re looking for. This should not be something as simple as looking
# for, like, the word “public” – it’s totally reasonable to make a variable that is just named “public” in Python!

# • Global variables are often bad coding practice unless they are constants that are referenced without
# modification. Search for any global variables that are modified inside a function.

# • Either in combination with the above bullet or separately, search for any local variables that are given the same
# name as global variables – also not an error, but inadvisable.

# • Find indentation errors (that is, an increase in indentation level not preceded by something that forms a code
# block, or a decrease in indentation level that doesn’t match a prior indentation level.)

# • Find missing colons.

# • I’m sure there are tons of these I haven’t thought of. Feel free to propose any that I haven’t thought of – I may
# add them to this assignment in the future! They can be mistakes or bad coding practices.