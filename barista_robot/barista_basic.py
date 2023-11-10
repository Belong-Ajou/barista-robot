from barista_template import BaristaTemplate
from robot_controller.robot_behavior import RinseBehavior,SkipRinse

class BaristaBasic(BaristaTemplate):
    def _rinse(self):
        rinse_action = RinseBehavior(SkipRinse())
        rinse_action.rinse()
        return
    
    def _place_coffee_grounds(self):
        print("Place the coffee grounds in the filter paper.")
        return
    
    def _bloom(self, time: int, amount: int):
        print("Bloom: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        return 
    
    def _pour(self, time: int, amount: int):
        print("Pour: Pour in {0} grams of hot water, wait {1} seconds".format(str(amount), str(time)))
        return 
    
    def _wait(self, time:int):
        print("Wait {0} seconds".format(str(time)))

    def _exit(self):
        print("Enjoy you coffee!")
        return 
    
if __name__ == "__main__":
    my_recipe = {"bloom":[10, 100], "pour": [10, 90], "wait":[120]}
    barista = BaristaBasic("192.168.58.2")
    barista.make_coffee(my_recipe)