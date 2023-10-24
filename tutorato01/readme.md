
# Ascii characters 

**GOAL** implements a function to print the ascii characters from 32 to 127. For example, if we write a .py file and we run it `asciitable.py` we obtain the following:

```bash
./asciitable.py
```

| Dex Hex Chr | Dex Hex Chr | Dex Hex Chr |
|:-----------:|:-----------:|:-----------:|
| 32  20      | 64  40   @  | 96  60   `  |
| 33  21   !  | 65  41   A  | 97  61   a  |
| 34  22   "  | 66  42   B  | 98  62   b  |
| 35  23   #  | 67  43   C  | 99  63   c  |
| 36  24   $  | 68  44   D  | 100  64   d |
| 37  25   %  | 69  45   E  | 101  65   e |
| 38  26   &  | 70  46   F  | 102  66   f |
| 39  27   '  | 71  47   G  | 103  67   g |
| 40  28   (  | 72  48   H  | 104  68   h |
| 41  29   )  | 73  49   I  | 105  69   i |
| 42  2a   *  | 74  4a   J  | 106  6a   j |
| 43  2b   +  | 75  4b   K  | 107  6b   k |
| 44  2c   ,  | 76  4c   L  | 108  6c   l |
| 45  2d   -  | 77  4d   M  | 109  6d   m |
| 46  2e   .  | 78  4e   N  | 110  6e   n |
| 47  2f   /  | 79  4f   O  | 111  6f   o |
| 48  30   0  | 80  50   P  | 112  70   p |
| 49  31   1  | 81  51   Q  | 113  71   q |
| 50  32   2  | 82  52   R  | 114  72   r |
| 51  33   3  | 83  53   S  | 115  73   s |
| 52  34   4  | 84  54   T  | 116  74   t |
| 53  35   5  | 85  55   U  | 117  75   u |
| 54  36   6  | 86  56   V  | 118  76   v |
| 55  37   7  | 87  57   W  | 119  77   w |
| 56  38   8  | 88  58   X  | 120  78   x |
| 57  39   9  | 89  59   Y  | 121  79   y |
| 58  3a   :  | 90  5a   Z  | 122  7a   z |
| 59  3b   ;  | 91  5b   [  | 123  7b   { |
| 60  3c   <  | 92  5c   \  | \| 124  7c  |
| 61  3d   =  | 93  5d   ]  | 125  7d   } |
| 62  3e   >  | 94  5e   ^  | 126  7e   ~ |
| 63  3f   ?  | 95  5f   _  | 127  7f     |

As first step, let's create a file and make it executable:

```bash
touch asciitable.py
chmod u+x asciitable.py
```

Now open the file with a text editor - we recommend Visual Studio Code- and do the following :

1. Make sure the file invoke the python interpreter
2. Implement a `print_ascii_table_block` that for a give integer prints the char and its hexadecimal value
3. Implement a `print_ascii_table` to print the whole table

## Suggested settings

Enable visual studio code autosave

https://code.visualstudio.com/docs/editor/codebasics#_save-auto-save


## Exercises

- Expand the table to print an additional column with the value from 0 to 32. These value are not printable character, so we cannot use the `chr` function to print a char. Where can we take the value from?  
**Hint** list can be used to store string values. 
 
- Create a `base64.py` program to print the base64 table

## Reference

- https://realpython.com/python-shebang/
- https://realpython.com/python-f-strings/
- https://www.geeksforgeeks.org/python-lists/
