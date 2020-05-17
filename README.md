LANGUAGUE: Python

CORE FUNCTION:
    Basic compiler going to contains: 
    - Tokenizer 
    - Parser 
    - Abstract syntax tree (AST) 
    - Code generation 
    - Optimization (if possible)

    Now, you'll have to think about these things: 
    - Token class
        + Data type: array (?)

    - AST class
        + Data type: Python dictionary (?)
        + 
    - Tree traversal algorithm (Depth-first)
    - Transform token into AST
    - Code generation from AST

ADDITIONAL: 
    - Text editor 
    - Syntax highlight
    - Support compile inside text editor (Simple IDE)
        + Implement VIM as text editor 
    - Write document and syntax instructions  

FILE EXTENSION: 
    - *.bb

FEATURES: 
    - THINKING ABOUT WRITING FUNCTION (SUBPROGRAM) 
        + CONCERT about function name (SUBPROGRAM NAME)
    - ERROR, WARNING 
    - Support comment
    - LOCAL and GLOBAL VARIABLES 
    - PASSING: 
        + Pass-by-value 
        + pass-by-result
        + pass-by-reference
        + pass-by-value-result

CONCERN: 
    - RULES FOR FUNCTION NAMES AND VARIABLES NAME
    - Limit input, object passing and memory CONCERN
    - NEGATIVE variable (?)
    - SYNTAX END command (?) 
    - DISTINGUISH BETWEEN INTERPRETER AND COMPILER 
        -> INTERPRETER: act on what program tell it to do 
        -> COMPILER: transform into machine language 
        -> Plan right now is to build interpreter first and then 
            re-used some of the code to build compiler  
    - Learn about regular expression 



REFERENCES: 
	https://github.com/dxv2k/the-super-tiny-compiler
	https://github.com/peternguyen93/Barebones-Compiler
    https://github.com/dxv2k/barebones
    Computer Science An Overview 12th Edition 
    Computer Science An Overview 9th Edition 
    https://ruslanspivak.com/lsbasi-part1/ [CURRENTLY WATCHING]




