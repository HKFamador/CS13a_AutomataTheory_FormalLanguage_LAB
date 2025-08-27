def dfa2(string):
    state = 'q0'
    for ch in string:
        if state == 'q0':
            if ch == 'a':
                state = 'q1'
            elif ch == 'b':
                state = 'q2'
            else:
                return None
        elif state == 'q1':
            if ch == 'a':
                state = 'q0'
            elif ch == 'b':
                state = 'q3'
            else:
                return None
        elif state == 'q2':
            if ch == 'a':
                state = 'q3'
            elif ch == 'b':
                state = 'q0'
            else:
                return None
        elif state == 'q3':
            if ch == 'a':
                state = 'q2'
            elif ch == 'b':
                state = 'q1'
            else:
                return None
    return state == 'q3'


if __name__ == "__main__":
    while True:
        string = input("Enter a string (a's and b's only): ").strip()
        result = dfa2(string)

        if result is None:
            print("❌ Invalid input: only 'a' and 'b' allowed")
        elif result:
            print("result: ACCEPTED ✅")
        else:
            print("result: REJECTED ❌")

        again = input("Try again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

#Sample Accepted : ab, abbaba, babaab
#Sample Rejected : abab, babaa, ababbba
