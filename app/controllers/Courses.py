

from system.core.controller import *


class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('CourseModel')
        self.db = self._app.db
# display the main page
    def index(self):
        courses = self.models['CourseModel'].get_all_courses()
        return self.load_view('index.html', courses=courses)

# Creating the Add courses into the query

    def add(self):
        name = request.form['name']
        description = request.form['description']

        data = {
            'name': name,
            'description': description
        }
        if len(name) < 5:
            flash("Course Name Cannot be Empty*")
        elif len(description) < 15:
            flash(" Need more information in description*")
        else:
            self.models['CourseModel'].add_course(data)

        return redirect('/')
# This will show the delete page
    def destroy(self,id):
        course = self.models['CourseModel'].get_course_by_id(id)
        return self.load_view('destroy.html', course = course)

    def remove(self,id):
      
        self.models['CourseModel'].remove_course(id)
        return redirect('/')


    
        

    

