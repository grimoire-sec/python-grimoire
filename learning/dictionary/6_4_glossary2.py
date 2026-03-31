glossary = {'integer' : 'An integer is a whole number without any decimal places.',
            'string' : 'A string is a sequence of characters — text enclosed in quotes.', 
            'list' : 'A list is an ordered collection of values enclosed in square brackets.',
            'program' : 'A program is a collection of code that performs a specific task or set of tasks.',
            'function' : 'A function is a reusable block of code that performs a specific action.',
            'dictonary' : 'A collection of key-value pairs, where each key maps to a value. Dictionaries are unordered, mutable, and defined using curly braces.',
            'loop' : 'A control structure that repeatedly executes a block of code. Python has two main types: for loops (iterate over a sequence) and while loops (run as long as a condition is true).',
            'variable' : 'A named container that stores a value in memory. Variables are created by assignment and can hold any data type.',
            'boolean' : 'A data type with only two possible values: True or False. Booleans are commonly used in conditions and comparisons.',
            'class' : 'A blueprint for creating objects. It defines a set of attributes (data) and methods (functions) that the created objects will have. Classes are the foundation of object-oriented programming in Python.'}

for k, v in glossary.items():
    print(f'\n{k}:\n\t{v}')