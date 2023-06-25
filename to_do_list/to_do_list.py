import os
import argparse


class ToDoList:
    def __init__(self):
        self.todo = []
        self.text_path = os.path.expanduser('~/to_do_list.txt')
        self.read_list()

    def read_list(self):
        # 저장된 리스트 보여주기
        if os.path.exists(self.text_path):
            with open(self.text_path, "r") as f:
                lines = f.readlines()
                new_list = []
                for text in lines:
                    new_list.append(text.rstrip())
                self.todo = new_list

    def save_list(self):
        # 리스트 text file로 저장
        with open(self.text_path, "w") as f:
            for text in self.todo:
                f.write(text + '\n')

    def print_list(self):
        # To Do List 보여줌
        print("""
        ------------------------  To Do List  ------------------------
        """)

        for idx, text in enumerate(self.todo):
            print(f'\t\t{idx +1} - {text}')

        print("""
        --------------------------------------------------------------
        
        """)

    def add_item(self, item):
        # 리스트 추가
        self.todo.append(item)
        self.save_list()
        self.print_list()

    def edit_item(self, idx):
        # 리스트 수정      
        item = input("수정할 내용을 입력하세요.")
        self.todo[int(idx)-1] = item
        self.save_list()
        self.print_list()
        
    def delete_item(self, idx):
        # 리스트 삭제
        del self.todo[int(idx)-1]
        self.save_list()
        self.print_list() 


def main():
    todo = ToDoList()

    todolist = argparse.ArgumentParser()
    todolist.add_argument("-a", "--add", help = "추가")
    todolist.add_argument("-e", "--edit", help = "수정")
    todolist.add_argument("-d", "--delete", help = "삭제")
    args = todolist.parse_args()

    if args.add:
        todo.add_item(args.add)
    elif args.edit:
        todo.edit_item(args.edit)
    elif args.delete:
        todo.delete_item(args.delete)
    else:
        todo.print_list()
     

if __name__ == "__main__":
    main()
