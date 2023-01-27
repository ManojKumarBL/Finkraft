from difflib import SequenceMatcher 
def longest(s1,s29):
    seq_match= SequenceMatcher(None,s1,s2)
    match=seq_match.find_longest_match(0,len(s1),0,len(s2))
    if(match.size!=0):
        return(s1[match.a: match.a+match.size] )
    else:
        return('Longest Substring')
s1='abcdefgh'
s2='awysnfkfvn'
print("Original substring",s1+"\n",s2)
print("Comman largest substring:")
print(longest(s1,s2))