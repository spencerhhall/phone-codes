# phone-codes
---
	1-800-IMBORED is a lot easier to remember than 1-800-4626733.
For that reason, most numbers on phone keypads are associated
with a certain set of letters. The associations are standardized
as follows:\
\
`0- no letters\
1- no letters\
2- abc\
3- def\
4- ghi\
5- jkl\
6- mno\
7- pqrs\
8- tuv\
9- wxyz\`
\
For many people's phone passwords, they often choose to spell out
a word. It can be meaningful or completely random and it happens a lot.
For example, my mother's phone password used to be 3825 for a number
of years.\
\
This project seeks to find the most common 4 and 6-digit passcodes
(2 of the iPhone numerical passcode options) from a list of many 4
and 6 letter-long words. The results will be displayed graphically
(I need to work on my Python data visualization) so that you can
understand the odds of guessing a word-based passcode.\
\
For now, I will not be considering passcodes made from multiple words
or the commonality of the word itself because I haven't even finished
writing this file and that's gonna take some work. I'll probably incorporate
the "popularity" of words later on, but not yet.\
\
Idea: generalize it so that it just takes in a wordlist in standard format
and converts it into a set of numbers, which is displayed. It's on the user
to choose a good wordlist (popular words, length of words, etc.).