import sys

def read_file(path):
    #TODO: option break at some marked lines only, not every line
    with open(path, "r") as myfile:
        data = myfile.readlines()
    return data

def sanitize_text(text):
    san_text = []
    for line in text:
        san_line = line.replace("\n", "")
        if len(san_line)>0:
            san_text.append(san_line)
    return san_text

def merge_dialog(text):
    merged_text = []
    newline = str()
    for line in text:
        if line.startswith('-') or line.startswith('\"') or line.startswith('“') or line.endswith(':'):
            if len(newline)!=0:
                newline += '\n'
            newline += line
        else:
            if len(newline)!=0:
                merged_text.append(newline)
                newline = str()
            merged_text.append(line)
    return merged_text

def create_reversed(text, width = 60, separator='* \t *'):
    rev = []
    for line in reversed(text):
        rev.append(separator)
        rev.append(line)
    return rev

def save_reversed(text,path):
    with open(path, "w") as save_file:
        for line in text:
            save_file.write(line+'\n')

def main():
    path = sys.argv[1]
    text = read_file(path)
    text = sanitize_text(text)
    text = merge_dialog(text)
    rev_text = create_reversed(text)
    save_reversed(rev_text, ''.join(path.rsplit('.')[:-1]) + '_rev.txt')


if __name__ == "__main__":
    main()