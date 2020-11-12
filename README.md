This package was created to create simple spreadsheets of opcodes as part of the RISC V Architecture. 

Using this package is relatively straightforward:

1. Open opcode-formats in a text editor
2. Place any args you want to add under ##ARGLUTS. Bear in mind they must follow the format of a dictionary in Python (arglut['argname'] = (n, n)). The bit range must be expressed as a tuple.
    2a. If an arglut appears is formatted differently than its name implies, you must also add to the arglut_format dictionary. The key is the name of the arg while the value is the item this code will actually parse. A "|" represents a break, while ":" colon separates a range. So for example 'imm[20|10:1|11|19:12]' takes up bits 20, 10 to 1, 11, and 19 to 12.
3. Make sure there is an empty line separating the argluts/arglut_formats and ##OPCODES. The code will not function otherwise.
4. Place any opcodes you want to add under ##OPCODES, separated by newlines (enter/return). The format is hard to describe, but just follow what's already written
5. Run main, if all goes well, an excel spreadsheet will appear in the parse folder. You can then open that up and format it to whatever you want.