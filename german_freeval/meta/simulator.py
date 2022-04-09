from german_freeval.meta.context import Context


class Simulator:

    context: Context

    def __init__(self, context: Context) -> None:
        self.context = context

    def run(self):
        pass
