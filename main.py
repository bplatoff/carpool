from rider_class import Rider
from course_class import Course

#Need to define general program flow
#create a rider object
rider1 = Rider(1)
course1 = Course(11, False)
rider1.add_course(course1)
rider1.set_course_driver_status(course1, True)
print(rider1.rider_id)