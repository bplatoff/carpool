class Schedule:
    def __init__(self):
        self.course_list = []

    def add_course(self, new_course):
        if not self.contains_course(new_course):
            self.course_list.append(new_course)

    def remove_course(self, removable_course):
        if self.contains_course(removable_course):
            self.course_list.remove(removable_course)

    def set_course_driver_status(self, changeable_course, driver_status):
        for course in self.course_list:
            if changeable_course.course_id == course.course_id:
                course.change_driver_status(driver_status)

    def contains_course(self, checked_course):
        contains_bool = False
        for course in self.course_list:
            if checked_course.course_id == course.course_id:
                contains_bool = True
        return contains_bool
