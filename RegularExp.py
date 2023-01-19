# \d  -> all valid integers
# \D -> everything but the integers

#(^ and $ are positions) ^-> start of the string $-> end of a string
#([a-t],\w) describe set of characters
#(+,*,{9}) -> Quantifiers. How many times somethig as occured

#Ex- Francois, Mike Whitney, Sagun Khatri,Nick Francesco,Pickles,K5ANR
# Fran --> will look through strings for this 4 letters in the exact order. Will match "Francois" and "Nick Fransesco"
# ^ -> is used to match the start of a string. ^Fran -> Will only match Francois
# $ -> to match the end of a string -> i$ -> all string that ends with the letter i. Ex- "Sagun Khatri"
# \d -> to match a numerical digit -> will look for single numerical digit. 0-9. K5ANR
# \d\d -> No match. No name has two consecutive numerical digits
#\s -> to match white space. Will match any name that has a space.
#\w -> stands for word. will match any letter. Lower or Upercase, any digit or underscore. Will match every name cause every name has the charcaters
#^\w\w\w\w\s -> Will match any name that begins with consecutive word characters followed by a white space -> Mike Whitney, Nick Francesco

#https://www.youtube.com/watch?v=nxjwB8up2gI ->3:39





