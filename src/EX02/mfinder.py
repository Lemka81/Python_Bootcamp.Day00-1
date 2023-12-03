import sys

def valid_0(line):
    return line.startswith("*") and line.endswith("*") and\
            line[1] != "*" and line[2] != "*" and line[3] != "*"

def valid_1(line):
    return line.startswith("**") and line.endswith("**") and\
            line[2] != "*"

def valid_2(line):
    return line.startswith("*") and line.endswith("*") and\
            line[1] != "*" and line[2] == "*" and line[3] != "*"
def main():
    m_flag = True
    for i in range(3):
        line = next(sys.stdin).strip()
        m_flag &= len(line) == 5
        
        if not m_flag:
            break
        
        if m_flag and i == 0:
            m_flag &= valid_0(line)
        elif m_flag and i == 1:
            m_flag &= valid_1(line)
        elif m_flag and i == 2:
            m_flag &= valid_2(line)
        
    print(m_flag)


if __name__ == "__main__":
    main()