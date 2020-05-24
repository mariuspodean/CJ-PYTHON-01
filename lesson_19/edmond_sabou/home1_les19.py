
from contextlib import contextmanager


data = {
    "Name": "Ubuntu",
    "Version": "20.04",
    "Install": "apt",
    "Owner": "Canonical",
    "Kernel": "5.4.0",
    "Shell": "bash 5.0.16"
}


@contextmanager
def file(filename, method):
    print("__enter__")
    file = open(filename, method)

    error = ""

    try:
        yield file  # file = object
    except KeyError:
        error = "Key not found!"
    except IndexError:
        error = "Index error!"
    finally:
        print("__exit__")
        file.close()
        if error:
            print(error)


with open("text_file.txt", "w") as f:
    print("middle")
    f.write(str(data))
