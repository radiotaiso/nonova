from itertools import count
from subprocess import check_output
import logging

# class Activity(Object):


class Activity():
    _ids = count(0)

    def __init__(self, Project=None, Category=None, Ticket=None, Hours=None, Comment=None):
        self.id = self._ids.next()
        self.attribute_list = ['project', 'category', 'hours', 'comment']
        self.project = Project
        self.category = Category
        self.hours = Hours
        self.ticket = Ticket
        self.comment = Comment

    def toString(self):
        return "add -P {} -t {} -c {} {}".format(self.project, self.hours, self.category, self.comment)

    def insert_activity(self, pathToCli):
        self.fn = pathToCli + self.output
        p = check_output(self.fn)
        logging.info("insertando actividarks: ")
        logging.info(p)
        print p

# ------------ ENDS Activity class
