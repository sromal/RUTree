import requests

subject = "198"
link = "http://sis.rutgers.edu/oldsoc/courses.json?subject=" + subject + "&semester=12020&campus=NB&level=UG"
data = requests.get(link).text

class Course:
    name = ""
    id = ""
    prereqs = []