import pickle
import os

# 检测表情符号函数
def check_emoji(eva_t):
    str_new = ""
    for content in eva_t:
        if u"\U0001F600" <= content <= u"\U0001F64F":
            continue
        elif u"\U0001F300" <= content <= u"\U0001F5FF":
            continue
        elif u"\U0001F680" <= content <= u"\U0001F6FF":
            continue
        elif u"\U0001F1E0" <= content <= u"\U0001F1FF":
            continue
        else:
            str_new += content
    return str_new

def do_update(file_dir):
    pk_file = open(os.path.join(file_dir, 'eva.pkl'), 'rb')
    eva_list = pickle.load(pk_file)
    with open(os.path.join(file_dir, 'standard.txt', 'a')) as fileObj:
        for line in eva_list:
            try:
                fileObj.write(line + "\n")
            except Exception:
                # 符号检测和字符串重建
                eva = check_emoji(line)
                fileObj.write(eva + "\n")

if __name__ == "__main__":
    do_update()
