class RinseStrategy:
    def rinse(self):
        raise NotImplementedError
    
class SkipRinse(RinseStrategy):
    def rinse(self):
        print("Skip the step of rinse")

class Rinse(RinseStrategy):
    def rinse(self):
        print("Rinse the coffee filter paper")

class RinseBehavior:
    def __init__(self, strategy) -> None:
        self.strategy = strategy

    def rinse(self):
        self.strategy.rinse()

if __name__ == "__main__":
    rinse_action = RinseBehavior(SkipRinse())
    rinse_action.rinse()
    rinse_action = RinseBehavior(Rinse())
    rinse_action.rinse()