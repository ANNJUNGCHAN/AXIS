# 패키지 로더
import os
import shutil

# txt 파일 읽어오기

def open_txt(input_file) :
    
    with open(input_file, 'r') as file:
        lines = file.readlines()
        
    return lines

# 모든 클래스 값을 0으로 바꾸기

def oneclass_modify(lines) :
    
    modified_lines = []
    for line in lines:
        parts = line.split()
        parts[0] = '0'  # 클래스 값을 0으로 변경
        modified_line = ' '.join(parts)
        modified_lines.append(modified_line)
        
    return modified_lines

# 확률값 제거
def drop_probs(lines) :
    
    modified_lines = []
    
    for line in lines:
        parts = line.split()
        
        if len(parts) == 5 :
            pass
        
        else :
            parts = parts[0:5]
        
        modified_line = ' '.join(parts)
        modified_lines.append(modified_line)
        
    return modified_lines

# 바뀐 리스트를 txt 파일로 저장

def save_list_to_txt(path, save_list) :
    
    with open(path, 'w') as file:
        for line in save_list:
            file.write(line + '\n')

# 텍스트 파일에 데이터가 존재하는지 확인
def is_file_not_empty(file_path):
    """
    주어진 파일 경로의 텍스트 파일에 내용이 있는지 확인합니다.

    :param file_path: 확인할 텍스트 파일의 경로
    :return: 파일에 내용이 있으면 True, 없으면 False
    """
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if content.strip():
                return True
            else:
                return False
            
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return False
    
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        return False
    
# 파일이동 (jpg, bmp 식별기능 포함)
def file_mover(before_path, after_path, txt_path) :
    ### 이미지 파일의 확장자는 .jpg 또는 .bmp
    ### .jpg
    jpg = txt_path.replace('txt','jpg')
    ### .bmp
    bmp = txt_path.replace('txt','bmp')
    ### T/F
    isjpg = os.path.isfile(os.path.join(before_path,jpg))
    isbmp = os.path.isfile(os.path.join(before_path,bmp))
    ### isjpg로 jpg인지 bmp인지 확인
    if isjpg :
        ### txt move
        shutil.move(os.path.join(before_path, txt_path),os.path.join(after_path, txt_path))
        ### jpg move
        shutil.move(os.path.join(before_path, jpg),os.path.join(after_path, jpg))
    else :
        ### txt move
        shutil.move(os.path.join(before_path, txt_path),os.path.join(after_path, txt_path))
        ### bmp move
        shutil.move(os.path.join(before_path, bmp),os.path.join(after_path, bmp))