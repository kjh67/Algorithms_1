from functools import lru_cache

@lru_cache(maxsize=None)
def stair_combinations(n):
    if n <= 0:
        return 0
    elif n <= 2:
        return n
    else:
        return stair_combinations(n-1) + stair_combinations(n-2)

def main():
    print(stair_combinations(4))

if __name__ == "__main__":
    main()