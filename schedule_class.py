from course_class import Course

class Schedule:
    def __init__(self):
        self.course_list = []

    def add_course(self, new_course):
        self.course_list.append(new_course)

    def remove_course(self, removable_course):
        self.course_list.remove(removable_course)

    def set_course_driver_status(self, changeable_course, driver_status):
        for course in self.course_list:
            if changeable_course.class_id == course.class_id:
                course.change_driver_status(driver_status)