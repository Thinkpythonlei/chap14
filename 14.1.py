def main():
    s1 = 'aa'
    s2 = 'bbb'
    f1 = 'words.txt'
    f2 = 'words2.txt'
    sed(s1, s2, f1, f2)
#定义每个变量赋值



def sed(s1, s2, f1, f2):
    try:
        fin = open(f1, 'r')
        fout = open(f2, 'w')
    except:
        print('openError!')
    for s in fin:
        try:
            if (s.strip() == s1):
                fout.write(s2 + '\r\n')
            else:
                fout.write(s)
        except:
            print('writeError!')
    fin.close()
    fout.close()


# def main():
#     s1 = 'aa'
#     s2 = 'bbb'
#     f1 = 'words.txt'
#     f2 = 'words2.txt'
#     sed(s1, s2, f1, f2)


if __name__ == '__main__':
    main()