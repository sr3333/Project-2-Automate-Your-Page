# This python code is for Project 2: Automate your Page.
# It is an exercise to use Variables, Functions, Appropriate use of Data in nested lists and Appropriate use of other coding techniques using loop statements 

# The generate_concept_HTML is to provide the lay-out of how the result will be printed
# This def is the result from the execution of def make_HTML
# html_text_1 will be the value of the variable obtained from list in the string position 0, which will be called lesson_title
# html_text_2 will be the value of the variable obtained from list in the string position 1, which will be called description_header
# html_text_3 will be the value of the variable obtained from list in the string position 2, which will be called description
def generate_concept_HTML(lesson_title, description_header,description):
    html_text_1 = '''
<div class="concept">
    <div class="lesson_title">
        ''' + lesson_title + '''
        '''
    html_text_2 = '''
    </div>
    <div class="description_header">
        ''' + description_header
    html_text_3 = '''
        </div>
        <div class="description">
        ''' + description + '''
    </div>
</div>
        '''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# The make_HTML is to obtain the variables listed in the nested list called EXAMPLE_LIST_OF_CONCEPTS
# lesson_title will choose the string in the first position
# description_header will choose the string the second position
# description will choose the string the third position
# Once the strings are properly named it then returns the value into the def generate_concept_HTML to be prepared for the lay out of how it should be printed
def make_HTML(concept):
    lesson_title = concept[0]
    description_header = concept[1]
    description = concept[2]
    return generate_concept_HTML(lesson_title, description_header,description)

# EXAMPLE_LIST_OF_CONCEPTS this is the nested list of variables containing the notes.
EXAMPLE_LIST_OF_CONCEPTS = [['Lesson 1: Introduction to "Serious" Programming', 'Computer','''Most machines (like a toaster) are designed to do a few things. Unless you physically alter these machines, they will only be able to do those things. Computers are different. A computer can be programmed to do anything we want, as long as we can write a program that specifies a specific sequence of instructions.'''],[' ','Computer Program','A program is a precise sequence of steps that a computer can follow to do something useful. Web browsers, games, mobile apps, and simple print statements are all examples of computer programs.'],['','Programming Language','A programming language is what programmers use to tell a computer what to do. Python is one example of a programming language.'],['','Python','Python is a programming language. When you write Python code and press "Run", a Python Interpreter converts the code you wrote as a set of instructions that the computer itself can understand and execute.'],['','Grammar','''Just like human languages have grammars, programming languages do too. A grammar is a specification of what is "correct" and what is "incorrect." In languages like English, people can often make sense of sentences that aren't technically "correct," but computers aren't smart enough to do this. This means we have to write code that is exactly "correct" according to the Python interpreter, otherwise our code won't run.'''],[' ','Python Expressions','''A Python "expression" is a legal Python statement. For example: print 1 + 1 is a valid expression, but print 1 + (without a number at the end) is not. This video does a good job of explaining the Python grammar for "expressions".'''],['Lesson 2: Variables and Strings','What is a variable in Python?','''Variables give programmers a way to give names to values. If my_variable is a variable with a value of 2, then the following code would print out 4:

        print my_variable + my_variable

        What does it meant to assign a value to a variable? How is it done?
        We can assign the value 2 to the variable my_variable by writing code like this:

        my_variable = 2

        We can even change the value of a variable by re-assigning it to a different value later.

        What's the difference between what the equals sign means in 2 + 3 = 5 and my_variable = 5?
        In the line 2 + 3 = 5, the equals sign means "is the same as".

        In the line my_variable = 5, the equals sign means "takes the value of".

        What are some ways variables are useful?
        Variables can be useful to programmers in many ways:

        They improve code readability by using names that make sense to humans.
        They give us a way to store the value of important data.
        They give us a way to change the value of something (like in the line days = days-1
        What is the difference between 2 + 2 and "2" + "2"?
        In Python, 2 is a number while "2" is a string.

        The code 2 + 2 would give 4.

        The code "2" + "2" would give "22".'''],['Lesson 3: Input -> Function -> Output','What is a function (Dave calls them "procedures")?','''A function is something that takes input, does something to that input, and then produces output. For example, a function named square might take a number as input and produce the square of that number as output.

        What is the difference between making and using a function?
        Functions are made by starting a line of code with the keyword def and then giving a function name followed by the function parameters in parentheses. These parameters will eventually be replaced by actual values when the function is used (called).

        In the "body" of the function, we write the code that specifies what to do with the input parameters. For example the following code could be the definition of a function called square:

        def square(x): 
        answer = x * x 
        return answer
        To use a function, we write the name of the function followed by the value(s) we want to give it in parentheses. Like this:

        print square(4) 
        >>>16
        How do functions help programmers avoid repetition?
        Functions are tools that programmers can create and reuse forever! Once you've defined a function once, you never have to define it again.

        What happens if a function doesn't have a return statement?
        The return keyword tells Python exactly what the function should produce as output. If a function doesn't have a return statement, then you'll get behavior like this:

        def add_two(x): 
        answer = x + 2 

        new_number = add_two(7)
        print new_number
        >>>None''']]


# make_HTML_for_many_concepts this will search the nested list of variables that contains the notes from the nested list called EXAMPLE_LIST_OF_CONCEPTS
# This def will continue to search the nested list by using the 'for..in..' loop, until there is no other variables.
# This def also calls def make_HTML and place the value into concept_HTML.
# The value of concept_HTML is added into HTML until the first set of list variables are completed.  Once completed it will return the value into make_HTML_for_many_concepts
def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

# This will print out the result from def make_HTML_for_many_concepts using nested list EXAMPLE_LIST_OF_CONCEPTS
print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)