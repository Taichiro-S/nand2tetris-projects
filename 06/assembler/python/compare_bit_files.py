def compare_bit_files(file1, file2):
    with open(file1, 'rb') as f1:
        with open(file2, 'rb') as f2:
            f1 = f1.readlines()
            f2 = f2.readlines()
            if len(f1) != len(f2):
                print('different length')
                print(len(f1), len(f2))
                return
            is_same = True
            for i,line in enumerate(f1):
                byte1 = f1[i]
                byte2 = f2[i]
                if byte1 != byte2:
                    print('line' + str(i+1))
                    is_same = False
                    print('different')
                    l  = []
                    for i,s in enumerate(byte1):
                        l.append(i)
                    print(*l)
            if is_same:
                print('same')

INPUT_FILE1 = "/Users/sekiguchi/Documents/nand2tetris/projects/06/pong/myPong.hack"
INPUT_FILE2 = "/Users/sekiguchi/Documents/nand2tetris/projects/06/pong/Pong.hack"

compare_bit_files(INPUT_FILE1, INPUT_FILE2)
