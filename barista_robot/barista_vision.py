from barista_basic import BaristaBasic

class BaristaVision(BaristaBasic):
    def _rinse(self):
        print("Grap a kettle by visino")
        print("Rinse the coffee filter paper.")
        return
    
    def _place_coffee_grounds(self):
        print("Grap a cup of the grinded coffee and Locate over a dripper.")
        return super()._place_coffee_grounds()
    
if __name__ == "__main__":
    my_recipe = {"bloom":[10, 100], "pour": [10, 90], "wait":[120]}
    barista = BaristaVision("192.168.58.2")
    barista.make_coffee(my_recipe)