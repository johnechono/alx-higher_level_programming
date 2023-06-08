#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    arr = dir(hidden_4)

    for a in range(len(arr)):
        if (arr[a][:2] != "__"):
            print(arr[a])
