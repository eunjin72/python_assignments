import os
import re

'''
project 폴더에서 정보 가져오기
'''


project_path = r'C:/Users/jin91/PipelineTD/git/python_assignments/file_handling/project'

def get_project_list():
    project_list = os.listdir(project_path)
    print(project_list)

def get_seq_list(project_name):
    seq_path = project_path + os.path.sep + project_name + os.path.sep +'shot'
    seq_list = os.listdir(seq_path)
    print(seq_list)

def get_shot_list(project_name, seq_name):
    shot_path = project_path + os.path.sep + project_name + os.path.sep + 'shot' + os.path.sep + seq_name
    shot_list = os.listdir(shot_path)
    print(shot_list)

def get_path_info(path):
    path_info = {
        'project' : None,
        'sequence' : None,
        'shot' : None
    }

    m = re.search(r'C:/Users/jin91/project/(\w+)/shot/(\w+)/(\w+)/.+', path)
    if m:
        path_info['project'] = m.group(1)
        path_info['sequence'] = m.group(2)
        path_info['shot'] = m.group(3)

    print(path_info)

def get_path_info2(path):
    path_info = {
        'project' : None,
        'sequence' : None,
        'shot' : None
    }

    path_split = path.split('/')
    
    path_info['project'] = path_split[4]
    path_info['sequence'] = path_split[6]
    path_info['shot'] = path_split[7]

    print(path_info)


if __name__ == "__main__":
    get_project_list()
    get_seq_list('avata')
    get_shot_list('avata', 'boo')
    get_path_info(r'C:/Users/jin91/project/avata/shot/boo/0010/plate/v001')
    get_path_info2(r'C:/Users/jin91/project/avata/shot/boo/0010/plate/v001')

