#ファイルの読み込み

def load_file(fname):
    output=""
    with open(fname,"r",encoding="utf8")as reader:
        output=reader.read()


    if len(output)==0:
        raise Exception("ファイルがからの可能性があります")
    return output

if __name__=="__main__":
    print(load_file("uitest_url.txt"))