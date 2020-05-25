data = {
    "Name": "Ubuntu",
    "Version": "17.10",
    "Install": "apt",
    "Owner": "Canonical",
    "Kernel": "4.13"
}


class JustSomeExceptions:

    def __enter__(self):
        return "Does this have to return anything?"

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type == KeyError:
            print("KeyError occurred!")
            return True
        elif exc_type == IndexError:
            print("IndexError occurred")
            return True
        else:
            return False


#   No exception
with JustSomeExceptions() as f:
    print(data.keys())

#   KeyError
with JustSomeExceptions() as key:
    print(data[123])

#   IndexError
with JustSomeExceptions() as index:
    print(data["Name"][111])

#   Any other error
with JustSomeExceptions() as other:
    print(data.keys(123))
