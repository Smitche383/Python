class HighSchoolStudent(Student):

    school_name = "Lakewood High School"

    def get_school_name(self):
        return "This is a high school student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "_HS"
