from difflib import SequenceMatcher 
  
def longestSubstring(s1,s2): 
      seqMatch = SequenceMatcher(None,s1,s2) 
      match = seqMatch.find_longest_match(0, len(s1), 0, len(s2)) 
      if (match.size!=0): 
          print (s1[match.a: match.a + match.size])  
      else: 
          print ('No longest common sub-string found') 
if __name__ == "__main__": 
    s1 = str(input())
    s2 = str(input())
    longestSubstring(s1,s2) 
