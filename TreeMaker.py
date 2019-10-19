import requests
import json
import graphviz
import re

subject = "198"
link = "http://sis.rutgers.edu/oldsoc/courses.json?subject=" + subject + "&semester=12020&campus=NB&level=UG"
data = requests.get(link).text
courses = json.loads(data)
dot = graphviz.Digraph(comment='Tree')

for course in courses:
    dot.node(course["courseNumber"], course["courseNumber"] + " " + course["title"])
    prereqs = re.findall("\\d+:\\d+:\\d+", str(course["preReqNotes"]))

    for prereq in prereqs:
        if prereq[3:6] == subject:
            dot.edge(prereq[7:], course["courseNumber"])
            end = course["preReqNotes"].index(prereq[7:])
            start = course["preReqNotes"].find("and", end)
            possible = course["preReqNotes"][start + 5:start + 15]
            if possible[3:6] == subject:
                dot.edge(possible[7:], course["courseNumber"])
            break

dot.render('trees/' + subject + '.gv', view=True)
