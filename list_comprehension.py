# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
        x = int(input())
        y = int(input())
        z = int(input())
        n = int(input())

        results = []
        for i in  list(range(x+1)):
            for j in list((range(y+1))):
                for k in list((range(z+1))):
                    results.append([i,j,k])
                                                                  
        results1 = []
        for l in results:
        if sum(l) < n or sum(l) > n:
            results1.append(l)
        
        print(results1)
