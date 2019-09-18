import os
def clear_subfile(targetUrl):
    for file in os.listdir(targetUrl):
        path_file = os.path.join(targetUrl,file)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            clear_subfile(path_file)
            if len(os.listdir(path_file)) == 0:
                os.removedirs(path_file)
if __name__ == "__main__":
    clear_subfile("./result/")
