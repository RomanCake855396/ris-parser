import argparse

def authors(au):
    r=au.split(", ")
    if len(r)==2:
        return r[0]+" "+r[1][0]+"."
    if len(r)==1:
        return r[0]

def convert(ris_text):
    title=""
    journal=""
    year=""
    volume=""
    doi=""
    AU=[]
    for i in ris_text.splitlines():
        k,v=i.split("  - ")
        # print(k, v)
        match k:
            case "T1":
                title=v
            case "JO":
                journal=v
            case "PY":
                year=v
            case "VL":
                volume=v
            case "SP":
                sp=v
            case "DO":
                doi=v
            case "AU":
                au=v
                AU.append(authors(au))
    
    return f"{', '.join(AU)} {title}. // {journal}. {year}. {volume}. {sp}. DOI: {doi}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Перетворення RIS файлів у формат ДСТУ 8302-2015.")
    parser.add_argument("file", help="Шлях до RIS файлу для обробки")
    args = parser.parse_args()
    process_ris(args.file)
    with open(file_path, "r") as f1:
        s = f1.readlines()

    r=convert(s)
    print(r)