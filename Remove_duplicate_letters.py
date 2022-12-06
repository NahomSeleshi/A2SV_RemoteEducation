class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        frequency = Counter(s)
        stack = []
        currentLetters = set()
        for character in s:                
            while stack and character < stack[-1] and frequency[stack[-1]] and character not in currentLetters:
                currentLetters.discard(stack.pop())
            if not character in currentLetters:
                stack.append(character)
                currentLetters.add(character)
            frequency[character] -= 1            
        return "".join(stack)
                    
                 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
            