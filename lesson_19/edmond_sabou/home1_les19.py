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
def just_some_exceptions():
    # print("__enter__")

    error = ""

    try:
        yield "Returned object"  # file = object
    except KeyError:
        error = "Key not found!"
    except IndexError:
        error = "Index error!"
    finally:
        if error:
            print(error)


with just_some_exceptions() as f:
    print(data.keys())

#   KeyError
with just_some_exceptions() as key:
    print(data[123])

#   IndexError
with just_some_exceptions() as index:
    print(data["Name"][111])

#   Any other error
with just_some_exceptions() as other:
    print(data.keys(123))
