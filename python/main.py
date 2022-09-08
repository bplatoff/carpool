from rider_class import Rider
from course_class import Course

# Need to define general program flow
# create a rider object
# let's make it so that when a rider is created they can chose to add a car to be a driver
# tuple can be formatted
# (will drive (bool), car object (car_class), list of classes they're driving for (list or schedule))
rider1 = Rider(1)
# when the rider adds a course, if they're a driver they can choose to drive for the specific course
course1 = Course(11, False, 5)
rider1.add_course(course1)
rider1.set_course_driver_status(course1, True)
course2 = Course(12, False, 1)
rider1.add_course(course2)
# rider1.remove_course(course1)
print(rider1.rider_id)