import os


def concatenate_files(files):
    files_info = []
    for file in files:
        with open(os.path.join(os.path.dirname(__file__), file), encoding='utf-8') as f:
            lines = f.readlines()
            files_info.append([file, len(lines), lines])
    files_info_sorted = sorted(files_info, key=lambda file_length: file_length[1])
    with open(os.path.join(os.path.dirname(__file__), 'result.txt'), 'w') as f:
        for file in files_info_sorted:
            f.write(file[0] + '\n') 
            f.write(str(file[1]) + '\n') 
            for line in file[2]:
                f.write(line)
            f.write('\n')        
       
    
concatenate_files(['2.txt', '1.txt'])
