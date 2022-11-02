# Help
This application is used to convert Roman numerals to Arabic and vice-versa
## Below table shows the list of Roman symbols including their corresponding integer values

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
# Run instructions
```python
python3 roman_numeral_converter.py

select an option --roman or --numeral
Enter value Roman or Arabic number based on option choosed
#eg: roman_numeral_converter.py --numeral
```

### More features coming soon
Running application through cli using Click library

* **_--help_** :  help option will display the instructions on how to use this application.

* **_--numeral_** : numeral option will convert number to roman numeral

* **_--roman_** : roman option will convert to arabic numeral
