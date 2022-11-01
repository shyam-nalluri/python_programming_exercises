# Help

The Roman Numerals Converter Application aims to convert the given number to Roman numerals and vive versa. The application is to be coded in Python and deployed as a web application with Flask.

 As a first step is to write program that converts the given number (between 1 and 3999) to the roman numerals and roman number (eg XXCX) to the arabic numeral.


 Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
| Roman         | Arabic          |
| ------------- |:---------------:|
| I             |1                |
| V             |5                |
| X             |10               |
| L             |50               |
| C             |100              |
| D             |500              |
| M             |1000             |

```
There were certain rules that the numerals followed which should be observed.

1.	The symbols 'I', 'X', 'C', and 'M' can be repeated at most 3 times in a row.
2.	The symbols 'V', 'L', and 'D' can never be repeated.
3.	The '1' symbols ('I', 'X', and 'C') can only be subtracted from the 2 next highest values ('IV' and 'IX', 'XL' and 'XC', 'CD' and 'CM').
4.	Only one subtraction can be made per numeral ('XC' is allowed, 'XXC' is not).
5.	The '5' symbols ('V', 'L', and 'D') can never be subtracted.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.
```

- User input can be either integer or string, thus the input should be checked for the followings,

   - The input should be a decimal number within the range of 1 to 3999 or Roman numbers.

   - If the input is less then 1 or greater then 3999, user should be warned using the given html template.

   - If the integer is given as input roman number it will throw an error

   # Folder Structure
```css
Flask
--application
   --__init__.py
   --roman_numeral_converter.py
--static
   --style.css
   --index_html.css
--templates
   --index.html
   --result_arabic.html
   --resylt_roman.html
app.py
Readme.md

```

# How to setup and Run the flask server

```python
pip install flask
#create virtual env for flask


```
