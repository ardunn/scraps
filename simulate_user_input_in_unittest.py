# Fro


class SimulatedInput:
    """
    Adapted from https://stackoverflow.com/questions/39506572/how-to-test-function-that-has-two-or-more-inputs-inside
    """
    def __init__(self, *args):
        self.args = iter(args)

    def __call__(self, x):
        try:
            return next(self.args)
        except StopIteration:
            raise Exception("No more input")


# Then, in your test method
def test_some_function(self):
    codefile.input = SimulatedInput("u","v")
    codefile.some_function() . . . .
