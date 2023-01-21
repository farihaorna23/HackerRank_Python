# print(ord("a")) #97
# print(ord("b")) #98
# print(ord("c")) #99

def designerPdfViewer(h, word):
    height = 0
    # assuming all letters are not capital letters
    for letter in word:
        index_letter = ord(letter) - ord("a")
        height = max(height,h[index_letter])
  

    width = len(word)
    return height * width

print(
designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],"abc"))
    