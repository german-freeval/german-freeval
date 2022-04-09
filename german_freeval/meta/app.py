from german_freeval.meta.context import Context
from german_freeval.meta.simulator import Simulator


class App:
    """App is the main class of the german_freeval package.

    It initializes the configuration and starts a simulation.
    """

    def main(self, file: str):
        """Starts a simulationusing the configuration defined in the given file.

        Args:
            file (str): path to the config file to be used in the simulation
        """
        context = Context.create_from(file=file)

        Simulator(context=context).run()
