# -*- coding:utf-8 -*- 
__author__ = 'Vincent'
__date__ = '2017/9/11 11:45'


import xadmin

from .models import *


class CourseAdmin(object):
    pass


class LessonAdmin(object):
    pass


class VideoAdmin(object):
    pass


class CourseResourceAdmin(object):
    pass


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
