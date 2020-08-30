if __name__ == '__main__':
        n = int(input())
        arr = map(int, input().split())
        arr1 = sorted(list(set(list(arr))))
        x = len(arr1)
         print(arr1[x-2])

