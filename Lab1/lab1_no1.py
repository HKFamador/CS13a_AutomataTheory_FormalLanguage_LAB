def dfa1(string):
    # States: a (start), b, 1 (final)
    state = 'a'
    for ch in string:
        if state == 'a':
            if ch == '0':
                state = 'a'
            elif ch == '1':
                state = 'b'
            else:
                return None
        elif state == 'b':
            if ch == '0':
                state = '1'
            elif ch == '1':
                state = 'a'
            else:
                return None
        elif state == '1':
            if ch == '0':
                state = 'b'
            elif ch == '1':
                state = '1'
            else:
                return None
    return state == '1'


if __name__ == "__main__":
    while True:
        string = input("Enter a binary string (0s and 1s): ").strip()
        result = dfa1(string)

        if result is None:
            print("❌ Invalid input: not a binary string")
        elif result:
            print("result: ACCEPTED ✅")
        else:
            print("result: REJECTED ❌")

        again = input("Try again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break


#Sample Accepted : 101, 10001, 0101
#Sample Rejected : 0100, 1001, 1010