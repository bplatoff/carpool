class Course:
    def __init__(self, class_id, is_driver):
        self.class_id = class_id
        self.is_driver = is_driver

    def change_driver_status(self, driver_status):
        self.is_driver = driver_status
