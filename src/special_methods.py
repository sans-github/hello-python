class MyClass:
    """
    Experiment dunder methods: object lifecyecle, string representation etc.
    See `Special method names <https://docs.python.org/3/reference/datamodel.html#special-method-names>`_ for more info.
    """

    @staticmethod
    def static_method():
        print("I am static")

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"str: num1={self.num1}, num2={self.num2}"

    def __repr__(self):
        return f"repr: num1={self.num1}, num2={self.num2}"

    def instance_method(self):
        self.num1 = 2 * self.num1
        self.num2 = 2 * self.num2
        print(f"instance_method: num1={self.num1}, num2={self.num2}")


if __name__ == "__main__":
    myClass = MyClass("a", 3)
    print("\n\n")

    print(myClass.__str__())
    print("\n\n")

    print(myClass.__repr__())
    print("\n\n")

    myClass.instance_method()
    print("\n\n")

    myClass.static_method()
