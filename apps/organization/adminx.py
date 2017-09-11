# -*- coding:utf-8 -*- 
__author__ = 'Vincent'
__date__ = '2017/9/11 11:52'

from .models import *

import xadmin


class CityAdmin(object):
    pass


class OrgAdmin(object):
    pass


class TeacherAdmin(object):
    pass


xadmin.site.register(CityDict, CityAdmin)
xadmin.site.register(CourseOrg, OrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
