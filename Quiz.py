

class Quiz:
    wrong = 0
    right = 0

    def welcome(self):
        """
        This function handles user input(topic) and based
        on the input it will call the respective methods of
        the class
        """
        greet = "Welcome to the Quiz"
        width = 60

        def outline(string, length):
            return (string[0 + i:length + i] for i in range(0, len(string), length))

        print('+-' + '-' * width + '-+')

        for line in outline(greet, width):
            print('| {0:^{1}} |'.format(line, width))

        print('+=' + '=' * (width) + '=+')

        def options(option):
            for line in outline(option, width):
                print('| {0:^{1}} |'.format(line, width))

        options("  1. Basic Concepts")
        options("   2. Data Structures")
        options("3. Control flow")
        options("         4. Functions and Modules")
        options("            5. File & Exception handling")
        options("      6. Additional Concepts")
        options(" ")
        options("Note: *If in doubt copy the code and run it, *find any bugs? then let me know, Good Luck..!")

        print('+-' + '-' * (width) + '-+')

        user_input = False
        while user_input < 1 or user_input > 6:
            user_input = int(input("Choose a topic: ") or 0)
            if user_input == 1:
                self.basic_concepts()
            elif user_input == 2:
                self.data_structures()
            elif user_input == 3:
                self.control_flow()
            elif user_input == 4:
                self.functions_modules()
            elif user_input == 5:
                self.file_exception_handling()
            elif user_input == 6:
                self.additional_concepts()
            else:
                print("Please choose a right input(number)")

    def data(self):
        """
        This function prints out total attempts and failed attempts
        :return: Successful Attempts & Failed Attempts
        :rtype: str
        """
        print(f"Successful Attempts: {self.right}\nFailed Attempts: {self.wrong}")

    def layout(self, qn, question, options, correct):
        """
        Layout for questions, options. And this function
        handles user input(answers)
        :param qn: Question Number
        :type qn: int
        :param question: Question
        :type question: str
        :param options: Options
        :type options: str
        :param correct: Correct Answer
        :type correct: int
        :return: Layout for questions and options
        :rtype: str
        """
        print(f"Q{qn}")
        print(question)
        print("-" * 40)
        options = options.replace(";", "\n")
        print(options)
        print("-" * 40)
        user_input = False
        while user_input != correct:
            try:
                user_input = int(input("Enter your answer: ") or 0)
                if user_input == correct:
                    print("Yay(^_^) That's Right..!")
                    self.right += 1
                    break
                elif user_input == 100:
                    self.welcome()
                    break
                elif user_input == 111:
                    self.data()
                    exit()
                else:
                    print("Nope('_') try again..!")
                    self.wrong += 1
            except ValueError:
                print("Only integers(numbers) accepted..!")
            except Exception as e:
                print("Something went wrong..!", e)

        print("_" * 80)

    def quiz_finished(self):
        """This method will be called after completion of the quiz"""
        print("Congrats you have completed this module's quiz \n1. Restart \n2. Display result and Exit")
        ui = int(input("Enter your choice: "))
        if ui == 1:
            self.welcome()
        elif ui == 2:
            self.data()
            exit()
        else:
            print("Oops..! Wrong choice so restarting quiz....")
            self.welcome()

    def basic_concepts(self):
        print("_"*40+"Basic Concepts"+"_"*40)

        q1 = """print(\"hello world')\nwhat will be the output..?"""
        o1 = "1.hello world ;2.\"hello world' ;3.Error"
        self.layout(1, q1, o1, 3)

        q2 = "what are strings?"
        o2 = "1.anything between single or double quotes ;2.a data type ;3.represents text ;4.All the above"
        self.layout(2, q2, o2, 4)

        q3 = """str = "my name is James bond"\nprint (str.capitalize())\nOutput...?"""
        o3 = """1.My Name Is James Bond ;2.My name is james bond ;3.MY NAME IS JAMES BOND"""
        self.layout(3, q3, o3, 2)

        q4 = """data = int('223a')\nprint(type(data))\n"""
        o4 = """1.ERROR ;2.223 ;3.int ;4.223a"""
        self.layout(4, q4, o4, 1)

        q5 = """1str = 'hello world'\nprint(1str.upper())"""
        o5 = """1.HELLO WORLD ;2.'HELLO WORLD' ;3.Hello World ;4.ERROR"""
        self.layout(5, q5, o5, 4)


        q6 = """ui = input('Enter a number: ')\nprint(ui*2)\nEnter a number: 15\n\nWhat will be the output"""
        o6 = """1.30 ;2.1515 ;3.Error(Operation not possible between str and int) """
        self.layout(6, q6, o6, 2)

        q7 = """print(14+6*3)\nwhat will be the output?"""
        o7 = """1.23 ;2.32 ;3.60"""
        self.layout(7, q7, o7, 2)

        q8 = """print(4**2+(4-2)*4)\nwhat will be the output?"""
        o8 = """1.12 ;2.72 ;3.24"""
        self.layout(7, q8, o8, 3)

        q9 = """text = "python is fun!"\nprint(text[6:-1])"""
        o9 = """1.is fun ;2.is fun! ;3. is fun"""
        self.layout(9, q9, o9, 3)

        q10 = """text = 'What's The Time Right Now'\nprint(text.lower())"""
        o10 = """1.what's the time right now ;2.ERROR ;3.what's The Time Right Now"""
        self.layout(10, q10, o10, 2)

        self.quiz_finished()

    def data_structures(self):
        print("_" * 40 + "Data Structures" + "_" * 40)

        q1 = """x = 10, 25, 3.2\nprint(type(x))"""
        o1 = """1.int ;2.float ;3.tuple ;4.None """
        self.layout(1, q1, o1, 3)

        q2 = """data = [({2, 4}, {2, 5}), ({5, 3}), ({5, 5})]\n\nprint(type(data)) """
        o2 = """1.list ;2.tuple ;3.set ;4.Error"""
        self.layout(2, q2, o2, 1)

        q3 = """What are objects in python..?"""
        o3 = """1.Everything in Python treated as an object, including
variable, function, list, tuple, int, dictionary, set, etc 
;2.Objects are referred to the functions in python 
;3.Objects are functions with 'return' statement 
;4.All the Above """
        self.layout(3, q3, o3, 1)

        q4 = """my_list = [1, 2, 3]\n\nmy_list.append(5)\nmy_list.extend([7, 8])\nmy_list.insert(2, 10)\n\nprint(my_list)"""
        o4 = """1.[1, 2, 3, 5] ;2.[10, 1, 2, 3, 5, 7, 8] ;3.[1,2,3,5,7,8,10] ;4.[1,2,3,5,[7,8]]"""
        self.layout(4, q4, o4, 2)

        q5 = """x = {5, 3, 5, 9, 9.0, 9.01}\n\nprint(x)\nNote: elements are unordered"""
        o5 = """1.{9, 9.0, 9.01, 3, 5} ;2.{9, 9.01, 3, 5} ;3.{9, 9.0, 3, 5, 3, 9.01, 5}"""
        self.layout(5, q5, o5, 2)

        q6 = """letters = ['a', 'b', 'c']\nletters.insert(1, 'd')\n\nprint(letters[2])"""
        o6 = """1.c ;2.b ;3.d"""
        self.layout(6, q6, o6, 2)

        q7 = """nums = (2, 5, 6, 8)\nnums[1] = 15\nprint(nums)"""
        o7 = """1.(2, 15, 6, 8) ;2.(15, 5, 6, 8) ;3.Error"""
        self.layout(7, q7, o7, 3)

        q8 = """x = [2, 5, 7, 8, 10]\n\nprint(x[-3:-1])"""
        o8 = "1.[] ;2.[7, 8, 10] ;3.[8, 10] ;4.[7, 8]"
        self.layout(8, q8, o8, 4)

        q9 = """x = [2, 5, 7, 9]\n\nprint(x[:])"""
        o9 = "1.Error ;2.[] ;3.[2, 5, 7, 9]"
        self.layout(9, q9, o9, 3)

        q10 = "Which list slicing reverses the list 'nums'?"
        o10 = "1.nums[-1::] ;2.nums[::] ;3.[::-1] ;4.[:-1]"
        self.layout(10, q10, o10, 3)

        self.quiz_finished()


    def control_flow(self):
        print("_" * 40 + "Control Flow" + "_" * 40)

        q1 = """x = 15 < 15\nprint(x)\nwhat will be the output..?"""
        o1 = "1.True\n2.False"
        self.layout(1, q1, o1, 2)

        q2 = """x = 15\nx = x+5\nx += 25\nx -= 35\nwhat's the value x..?"""
        o2 = "1.10 ;2.45 ;3.30 ;4.15"
        self.layout(2, q2, o2, 1)

        q3 = "x = not(3 == 2)\ny = 25>25 or 23<26\nz = 65 != 65\nprint(x,y,z)\nOutput..?"
        o3 = "1.False True True ;2.False True False ;3.True True False ;4.True False False"
        self.layout(3, q3, o3, 3)

        q4 = """for i in '123':
    print(i) """
        o4 = "1.1\n  2\n  3 ;2.ERROR"
        self.layout(4, q4, o4, 1)

        q5 = """x = 12\ny = 18 \nif x = 12 and y = 15:
    print("True")\nelse:
    print("False")"""
        o5 = """1.True ;2.False ;3.ERROR """
        self.layout(5, q5, o5, 3)

        q6 = """for i in range(1, 10, 2):
    print(i)"""
        o6 = """1.2;  4;  6;  8;  10; ;2.1;  3;  5;  7;  9; ;3.2;  4;  6;  8"""
        self.layout(6, q6, o6, 2)

        q7 = """while False:
    print("Hello")"""
        o7 = """1.Infinite loop ;2.0 ;3.'Hello' ;4.No Output"""
        self.layout(7, q7, o7, 4)

        q8 = """x = 1\nli = []\nwhile x < 10:
    li.append(x)
    x += 2\n\nprint(li) """
        o8 = "1.[1, 2, 3, 4, 5, 6, 7, 8, 9] ;2.[0, 2, 4, 6, 8] ;3.[1, 3, 5, 7, 9]"
        self.layout(8, q8, o8, 3)

        q9 = """txt = ["Hello World"]\nfor char in txt:
    for i in char:
        print(i)"""
        o9 = "1.H;  e;  l;  l;  o;   ;  W;  o;  r;  l;  d ;;2.Error ;;3.Hello;  World"
        self.layout(9, q9, o9, 1)

        q10 = """car = {'name':'bmw', 'price':1200, 'model':2016}\nfor i, j in car:
    print(j, i)"""
        o10 = """1.bmw name\n  1200 price\n  2016 model ;2.Error ;3.name bmw\n  price 1200\n  model 2016"""
        self.layout(10, q10, o10, 2)


        self.quiz_finished()

    def functions_modules(self):
        print("_" * 40 + "Functions & Modules" + "_" * 40)

        q1 = """def my_func(name, age):
        return(f'{name} is {age} years old')\n\nprint(my_func(25, 'Bob')"""
        o1 = """1.25 is Bob years old ;2.ValueError ;3.TypeError"""
        self.layout(1, q1, o1, 1)

        q2 = """def is_adult(age=18):
    if age>18:
        return "Adult"
    else:
        return "Teen"\n\nprint(is_adult())"""
        o2 = "1.Teen ;2.adult ;3.TypeError"
        self.layout(2, q2, o2, 1)

        q3 = """def numbers(x):
    for i in range(x):
        return i\n\nprint(numbers(10))\n\nWhat will be highest number printed..?"""
        o3 = """1.10 ;2.9 ;3.0"""
        self.layout(3, q3, o3, 3)

        q4 = """def numbers(x):
    if x >= 15:
        return True
    elif x <15 and x>10:
        return False
    else:
        return True\n\nnumbers(12)\nwhat will be printed.?"""
        o4 = """1.True ;2.False ;3.No Output"""
        self.layout(4, q4, o4, 3)

        q5 = "from math import factorial as fcl \n\nHow do you call factorial function"
        o5 = "1.math.factorial ;2.factorial ;3.fcl"
        self.layout(5, q5, o5, 3)

        q6 = "from datetime import date\n\nprint(datetime.date.today())"
        o6 = "1.Current Date and time ;2.Current Date ;3.Error"
        self.layout(6, q6, o6, 3)

        q7 = """def greet(name):
    print(f"Hello {name}")
    return "Welcome"
    print("Have a nice day")\nprint(greet("Tahir"))"""
        o7 = "1.Hello Tahir\n  Welcome ;2.Hello Tahir\n  Welcome\n  Have a nice day ;3.Welcome 4.No output"
        self.layout(7, q7, o7, 1)

        q8 = """def add(x, y):
    return x+y

def calcee(num1, num2):
    if num1 % 2 == 0:
        return num1*num2
    else:
        return num1**num2

print(calcee(add(15, 0), 2))"""
        o8 = "1.30 ;2.Error ;3.4 ;4.225"
        self.layout(8, q8, o8, 4)

        q9 = "using which function we can combine 2 iterables"
        o9 = "1.zip ;2.map ;3.filter; "
        self.layout(9, q9, o9, 1)

        q10 = "num = -45.25\n\nprint(abs(num))"
        o10 = "1.-45.25 ;2.45.25 ;45.25 ;45.2"
        self.layout(10, q10, o10, 2)

        self.quiz_finished()

    def file_exception_handling(self):
        print("_" * 40 + "File & Exception Handling" + "_" * 40)

        q1 = "what can we do to the files using 'with' keyword..?"
        o1 = "1.only read a file ;2.only write a file ;3.only append a file ;4.all the above"
        self.layout(1, q1, o1, 4)


        q2 = "Using exception handling we can only handle RunTimeErrors(The Error which we get\
only at some specific situations)"
        o2 = """1.No we can handle Syntax and Logical Errors as well ;2.Yes we can only handle RuntTimeError"""
        self.layout(2, q2, o2, 2)

        q3 = """def test(num):
    if num != abs(num):
        raise ValueError
    else:
        return num**2

try:
    print(test('4'))
except ValueError:
    print('Only positive nums accepted')
except TypeError:
    print("Only int accepted")\n\nWhat will be the output"""
        o3 = "1.Only positive nums accepted ;2.Only int accepted ;3.16"
        self.layout(3, q3, o3, 2)

        q4 = """def test(num):
    if type(num) == str:
        raise TypeError
    elif num != abs(num):
        raise ValueError
    else:
        return num**2

print(test(-8))"""
        o4 = """1.ValueError ;2.TypeError ;3.64"""
        self.layout(4, q4, o4, 1)

        q5 = """try:
    print(5)
    print(5/0)
    print(10)
except ZeroDivisionError:
    print(15)
finally:
    print(30)\n\nWhich number will not be printed..?"""
        o5 = "1.15 ;2.10 ;3.30 ;4.5"
        self.layout(5, q5, o5, 2)

        q6 = """open('file.txt', '__') what should be written in the blank to read binary file"""
        o6 = """1.rb ;2.br ;3.r ;4.rab"""
        self.layout(6, q6, o6, 1)

        q7 = """file =  open('file1.txt', 'w')\nread = file.read()\n\nWhat will be the output"""
        o7 = """1.Display Content of file1.txt ;2.No output ;3.Error"""
        self.layout(7, q7, o7, 3)



        self.quiz_finished()

    def additional_concepts(self):
        print("_" * 40 + "Additional Concepts" + "_" * 40)

        q1 = """i = 0\nli = [i while True i = i+1]\n\nprint(li)"""
        o1 = """1.Creates an infinite num of list ;2.Error (Can't use while in list comprehension)"""
        self.layout(1, q1, o1, 2)

        q2 = "choose an option below to create a list like 'li = [0, 2, 4, 6, 8]' this using list comprehension"
        o2 = """1.li = [i for i in range(0, 10, 2)] ;
2.li = [i for i in range(10) if i % 2 == 0];
3.li = [i*2 for i in range(5)];
4.All the above can be used"""
        self.layout(2, q2, o2, 4)

        q3 = "my_func = lambda x, y, z : x+y+z, x-y-z\nprint(my_func(8, 4, 2))"
        o3 = "1.14,2 ;2.2,14 ;3.Error Coz lambda functions\
can have many parameters but only one expression "
        self.layout(3, q3, o3, 3)

        q4 = """test = lambda x : x**2\n\ndef main(num1, num2):
    if num1 > num2:
        return True
    elif num1 < num2:
        return False\n\nprint(main(test(4), 16))"""
        o4 = "1.True ;2.None ;3.False ;4.Error"
        self.layout(4, q4, o4, 2)

        q5 = "Following PEP 8(Best Practices to write python program) is:"
        o5 = "1.mandatory ;2.Not Important ;3.Recommended"
        self.layout(5, q5, o5, 3)

        self.quiz_finished()


start_quiz = Quiz()
start_quiz.welcome()