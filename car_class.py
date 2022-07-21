class Car:
    def __init__(self, car_id, driver_id):
        self.car_id = car_id
        self.rider_list = []
        self.driver_id = driver_id

    def add_rider(self, new_rider):
        if not self.contains_rider(new_rider):
            self.rider_list.append(new_rider)

    def remove_rider(self, removable_rider):
        if self.contains_rider(removable_rider):
            self.rider_list.remove(removable_rider)

    def contains_rider(self, checked_rider):
        contains_bool = False
        for rider in self.rider_list:
            if checked_rider.rider_id == rider.rider_id:
                contains_bool = True
        return contains_bool

    def change_car_driver(self, new_driver_id):
        consensus = True
        for rider in self.rider_list:
            if not rider.wants_trade:
                consensus = False
                print("Not all riders want a trade of driver")
            if not rider.trade_driver_id == new_driver_id:
                consensus = False
                print("Riders do not agree on new driver")

        if consensus:
            self.driver_id = new_driver_id
