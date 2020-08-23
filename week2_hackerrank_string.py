#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
        lines = line.split(" ")
            fixed_lines = "-".join(lines)
                return fixed_lines

            if __name__ == '__main__':


#https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
        return s.swapcase()


#https://www.hackerrank.com/challenges/whats-your-name/problem
def print_full_name(a, b):
        string = f"Hello {a} {b}! You just delved into python."
            return print(string)

#https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
        l = list(string)
            l[position] = character
                fixed_string = ''.join(l)
                    return fixed_string

                if __name__ == '__main__':
                        s = input()
                            i, c = input().split()
                                s_new = mutate_string(s, int(i), c)
                                    print(s_new)

# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    length = 0
        for i in range(0,len(string)-len(sub_string)+1):
                if string[i:i+len(sub_string)] == sub_string:
                            length += 1
                                return length

                                if __name__ == '__main__':
                                    string = input().strip()
                                        sub_string = input().strip()
                                            
                                            count = count_substring(string, sub_string)
                                                print(count))


#https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
        s = input()

            def fun1(s):
                        for i in range(len(s)):
                                        if(s[i].isalnum()):
                                                            return True;
                                                                        break;
                                                                            return False;

                                                                            def fun2(s):
                                                                                        for i in range(len(s)):
                                                                                                        if(s[i].isalpha()):
                                                                                                                            return True;
                                                                                                                                        break;
                                                                                            
                               return False;
def fun3(s):
            for i in range(len(s)):
                            if(s[i].isdigit()):
                                                return True;
                                                            break;
                                                                return False;

                                                                def fun4(s):
                                                                            for i in range(len(s)):
                                                                                            if(s[i].islower()):
                                                                                                                return True;
                                                                                                                            break;
                                                                                                                                return False;

                                                                                                                                def fun5(s):
                                                                                                                                            for i in range(len(s)):
                                                                                                                                                            if(s[i].isupper()):
                                                                                                                                                                                return True;
                                                                                                                                                                                            break;
                                                                                                                                                                                                return False;
                                                                                                                                                                                                
                                                                                                                                                                                                print (fun1(s))
                                                                                                                                                                                                    print (fun2(s))
                                                                                                                                                                                                        print (fun3(s))
                                                                                                                                                                                                            print (fun4(s))
                                                                                                                                                                                                                print (fun5(s))
                                                                                                                                                                                                                    
