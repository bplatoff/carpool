class Course:
    def __init__(self, course_id, is_driver):
        self.course_id = course_id
        self.is_driver = is_driver

    def change_driver_status(self, driver_status):
        self.is_driver = driver_status
