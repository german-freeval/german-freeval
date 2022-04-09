from german_freeval.meta.context import Context
from german_freeval.meta.simulator import Simulator


class App:
    def main(self, file: str):
        context = Context.create_from(file=file)

        Simulator(context=context).run()
