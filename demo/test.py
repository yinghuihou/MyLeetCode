import os


def main():
    aa = "  raaa.bbb.ccc.home"
    path = "import stat aaa.bbb.ccc.home;   "
    test = {}
    test["1"] = "hello"
    test["2"] = "nihao"
    test["1"] = "ppppp"

    li = path.strip().rstrip().split(" ")
    print(aa.strip()[0])



def delete_null_dir(dirr):
    if os.path.isdir(dirr):
        for p in os.listdir(dirr):
            d = os.path.join(dirr, p)
            if (os.path.isdir(d) == True):
                delete_null_dir(d)
    if not os.listdir(dirr):
        os.rmdir(dirr)


if __name__ == '__main__':
    main()
