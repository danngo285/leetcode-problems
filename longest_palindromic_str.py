def is_palindromic(substr: str) -> bool:
    if substr not in memorise:
        memorise.add(substr)
        if len(substr) <= 1:
            return True
        else:
            for i in range(int(len(substr)/2)):
                if substr[i] != substr[len(substr)- (i+1)]:
                    return False
            return True
def solution(full: str) -> bool:
    for i in range(len(full), 0, -1):
        j = 0
        while(i + j <= len(full)):
            if is_palindromic(full[j:i+j]):
                return(full[j:i+j])
            j += 1

if __name__ == '__main__':
    full = "ababa"
    global memorise
    memorise = set()
    print(solution(full))

