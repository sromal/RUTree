import requests
import json
import graphviz
import re

subject = "830"
link = "http://sis.rutgers.edu/oldsoc/courses.json?subject=" + subject + "&semester=12020&campus=NB&level=UG"
data = requests.get(link).text
courses = json.loads(data)
dot = graphviz.Digraph(comment='Tree')
for course in courses:
    dot.node(course["courseNumber"], course["courseNumber"] + " " + course["title"])
    prereqs = re.findall("\\d+:\\d+:\\d+", str(course["preReqNotes"]))
    masterPrereq = None
    for prereq in prereqs:
        if prereq[3:6] == subject:
            masterPrereq = prereq[7:]
            break
    if not masterPrereq == None:
        dot.edge(masterPrereq, course["courseNumber"])
dot.render('trees/'+subject+'.gv', view=True)
