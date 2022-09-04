from schedule_class import Schedule


class Rider:
    def __init__(self, rider_id):
        self.rider_id = rider_id
        self.car_list = []
        self.schedule = Schedule()

    def add_course(self, new_course):
        self.schedule.add_course(new_course)

    def remove_course(self, removable_course):
        self.schedule.remove_course(removable_course)

    def set_course_driver_status(self, course, driver_status):
        self.schedule.set_course_driver_status(course, driver_status)

    def request_car_driver_change(self, car_id, new_driver_id):
        for car in self.car_list:
            if car_id == car.car_id:
                car.trade_dict[self.rider_id] = (True, new_driver_id)
                car.change_car_driver(new_driver_id)
