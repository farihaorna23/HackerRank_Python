# \d  -> all valid integers
# \D -> everything but the integers

#(^ and $ are positions) ^-> start of the string $-> end of a string
#([a-t],\w) describe set of characters
#(+,*,{9}) -> Quantifiers. How many times somethig as occured

#Ex- Francois, Mike Whitney, Sagun Khatri,Nick Francesco,Pickles,K5ANR
# Fran --> will look through strings for this 4 letters in the exact order. Will match "Francois" and "Nick Fransesco"
# ^ -> is used to match the start of a string. ^Fran -> Will only match Francois
# + -> One or more occurrences -> "he.+o"
# * means "0 or more instances of the preceding regex token". Zero or more occurrences. 
# $ -> to match the end of a string -> i$ -> all string that ends with the letter i. Ex- "Sagun Khatri"
# \d -> to match a numerical digit -> will look for single numerical digit. 0-9. K5ANR
# \d\d -> No match. No name has two consecutive numerical digits
#\s -> to match white space. Will match any name that has a space.
#\w -> stands for word. will match any letter. Lower or Upercase, any digit or underscore. Will match every name cause every name has the charcaters
#^\w\w\w\w\s -> Will match any name that begins with consecutive word characters followed by a white space -> Mike Whitney, Nick Francesco

#Quantifiers
#Number of ways to spacify the number of copies of an expression
# [aeiou]}{2} -> will look for a string that has two consecutive vowels. The bracket is used to create a custom character set. ->Francois
# ^\w{7}$ -> searches for a string that has exactly 7 word characters
# \w{7} ->any name that containes 7 consecutive word characters


#Link
#https://www.w3schools.com/python/python_regex.asp
#https://www.youtube.com/watch?v=VU60rEXaOXk&list=PLGKQkV4guDKH1TpfM-FvPGLUyjsPGdXOg&index=1

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

txt = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

#["hello"]


#https://www.youtube.com/watch?v=nxjwB8up2gI ->3:39
import re

names =["Finn Bindeballe",
"Geir Anders Berge",
"HappyCodingRobot",
"Ron Cromberge",
"Sohil"]

#re.search(pattern,string)
#Find people with first and last name only
regex = '^\w+\s+\w+$' #two names with more than one white spaces

for name in names:
  result = re.search(regex,name)
  #<re.Match object; span=(0, 15), match='Finn Bindeballe'>
  #<re.Match object; span=(0, 13), match='Ron Cromberge'>
  if result:
    print(name)

#Search for word char sequence starting with C
regex1 = 'C\w*'

#if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#<re.Match object; span=(0, 17), match='The rain in Spain'
print(x)

txt1 = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x1 = re.findall("he.+o", txt1)

print(x1) #['hello']





