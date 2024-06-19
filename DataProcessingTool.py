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