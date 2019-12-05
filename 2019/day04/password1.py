min_ = 246540
max_ = 787419

if __name__ == "__main__":
    count = 0
    for n in range(min_, max_ + 1):
        digits = [int(d) for d in str(n)]
        assert len(digits) == 6
        increasing, double = True, False
        i = 0
        while i < len(digits) - 1:
            if digits[i] > digits[i + 1]:
                increasing = False
                break
            if digits[i] == digits[i + 1]:
                j = i + 1
                while (j < len(digits) - 1) and (digits[i] == digits[j + 1]):
                    j += 1
                if j == i + 1:
                    double = True
                i = j
            else:
                i += 1
        if increasing and double:
            print(n, "YES")
            count += 1
    print(count)
