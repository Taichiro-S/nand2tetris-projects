def compare_vm_files(file1, file2):
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
                vm1_line = f1[i]
                vm2_line = f2[i]
                if vm1_line != vm2_line:
                    print('line' + str(i+1))
                    is_same = False
                    print('different')
            if is_same:
                print('same')

VM1 = '/Users/sekiguchi/Documents/nand2tetris/projects/07/MemoryAccess/BasicTest/BasicTest_new.asm'
VM2 = '/Users/sekiguchi/Documents/nand2tetris/projects/07/MemoryAccess/BasicTest/BasicTest.asm'

compare_vm_files(VM1,VM2)
