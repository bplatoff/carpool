from schedule_class import Schedule
from course_class import Course

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