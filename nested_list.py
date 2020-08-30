if __name__ == '__main__':
        list1 = []
        list2 = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            list1.append([name, score])
        second_value = sorted(set([score for name, score in list1]))[1]
        for i in list1:
            if i[1] == second_value:
            list2.append(i[0])
            list2 = sorted(list2)
        print('\n'.join(list2))
