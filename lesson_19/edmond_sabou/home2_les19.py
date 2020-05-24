
data = {
    "Name": "Ubuntu",
    "Version": "17.10",
    "Install": "apt",
    "Owner": "Canonical",
    "Kernel": "4.13"
}


class JustSomeExceptions:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Enter")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")
        self.file.close()
        if exc_type == KeyError:
            print("KeyError occurred!")
        elif exc_type == IndexError:
            print("IndexError occurred")
        else:
            return True


with JustSomeExceptions("text_file.txt", "w") as f:
    print("Middle!")
    f.write("Hello!!")
