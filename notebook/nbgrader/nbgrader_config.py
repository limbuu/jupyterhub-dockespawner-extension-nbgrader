c = get_config()
c.Exchange.course_id = "course101"
c.Exchange.root = "/tmp/exchange"
c.CourseDirectory.root = '/home/jovyan/work/course101'
# ai-scholarship-program,if any changes occurs, COURSE_TO_HIDE variable must be changed in js/main.min.js

c.ExecutePreprocessor.timeout = -1
c.CourseDirectory.db_url = 'mysql+mysqlconnector://root:mysql123@172.20.0.2:3306/nbgrader_db'
#c.CourseDirectory.autograded_directory = '/home/jovyan/work/course101/autograded'