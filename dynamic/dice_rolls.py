from functools import lru_cache

@lru_cache(maxsize=None)
def dice_rolls(n, k, target):
    sum = 0
    # check that the target is achievable
    if not(target > n*k):
        for i in range(1, k+1):
            # if we only have one more dice, and it is the right value, take it
            if n == 1 and target == i:
                sum += 1
            # else if we have more than one dice, recurse
            elif target - i > 0 and n > 1:
                sum += dice_rolls(n-1, k, target-i)
            # final case: we have one dice left, but not the right value, so do nothing
    return sum

def main():
    x = dice_rolls(2,6,5)
    print(x)

if __name__ == "__main__":
    main()
