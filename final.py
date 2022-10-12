import BST
from termcolor import colored

def options():
    '''
    Prints Menu for operations
    '''
    options_list = ['Insert an item: type "insert [item]"', 
            'Inorder Traversal: type "inorder"',
            'Preorder Traversal: typr "preorder"',
            'Postorder Traversal: type "postorder"',
            'Levelorder Traversal: type "levelorder"',
            'Find an item: type "find [item]"', 
            'Erase an item: type "erase [item]"',
            'Clear all the data: type "clear"' ,
            'Height of tree: type "height"',
            'Number of nodes in tree: type "number of nodes"', 
            'Exit: type "0"']

    print("\nOPERATIONS MENU")
    for i, option in enumerate(options_list):
        print(colored(f'{i + 1}. {option}','green'))



if __name__ == '__main__':
    options()
    myBST = BST.BST()
    while True:
        command = input().split(' ')


        if command[0] == 'insert':
            if len(command) < 2 or command[1] == '':
                print(colored('error: Missing operand','red'))
            for i in range(1, len(command)):
                try:
                    myBST.insert(int(command[i]))
              
                except:
                    print(colored('input error','red'))

        if command[0] == 'inorder':
            if len(command) > 1:
                print(colored('error: no argument needed','red'))
            else:
                try:
                    print(colored('INORDER TRAVERSAL','blue'))
                    myBST.in_order()
                except:
                    print(colored('input error','red'))



        if command[0] == 'preorder':
            if len(command) > 1:
                print(colored('error: no argument needed','red'))
            else:
                try:
                    print(colored('PREORDER TRAVERSAL','blue'))
                    myBST.pre_order()
                except:
                    print(colored('error: no argument needed','red'))
                    

                    

        if command[0] == 'postorder':
            if len(command) > 1:
                print(colored('error: no argument needed','red'))
                
            else:
                try:
                    print(colored('POSTORDER TRAVERSAL','blue'))
                    myBST.post_order()
                except:
                    print(colored('input error','red'))
                    
        
        if command[0] == 'levelorder':
            if len(command) > 1:
                print(colored('error: no argument needed','red'))
                
            else:
                try:
                    print(colored('LEVELORDER TRAVERSAL','blue'))
                    myBST.level_order([myBST.get_root()])
                except:
                    print(colored('input error','red'))
                    



        if command[0] == 'find':
            if len(command) < 2 or command[1] == '':
                print(colored('error: Missing operand','red'))
                
            for i in range(1,len(command)):
                try:
                    print(myBST.find(int(command[i])))
                except:
                    print(colored('input error','red'))
                    
        
        if command[0] == 'clear':
            if len(command) > 1:
                print(colored('error: no argument needed','red'))
                
            else:
                try:
                    myBST.clear()
                    print('done')
                    print(colored("for operations menu type '1'",'yellow'))
                except:
                    print(colored('input error','red'))
                    



        if command[0] == 'erase':
            if len(command) < 2 or command[1] == '':
                print(colored('error: Missing operand','red'))
                
            for i in range(1, len(command)):
                try:
                    myBST.erase(int(command[i]))
                except:
                    print(colored('input error','red'))
                    
        

        if command[0] == 'number' and command[1] == 'of' and command[2] == 'nodes':
            if len(command) > 3:
                print(colored('error: no argument needed','red'))
                
            else:
                try:
                    print(colored('NUMBER OF NODES IS ' + str((myBST.get_number_of_nodes(myBST.get_root()))),'blue'))
                except:
                    print(colored('input error','red'))




        

        if command[0] == 'height':
            if len(command) > 1:
                print(colored('error: no argument needed','red'))
                
            else:
                try:
                    print(colored('HEIGHT OF TREE IS ' + str(myBST.height()),'blue'))
                except:
                    print(colored('input error','red'))
                    
        
        
        if command[0] == '1':
            if len(command) > 1:
                print(colored('input error','red'))
                
            else:
                options()

        if command[0] == '0':
            break
        

