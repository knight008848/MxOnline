# -*- coding:utf-8 -*- 
__author__ = 'Vincent'
__date__ = '2017/9/11 11:55'

from .models import *

import xadmin


class UserAskAdmin(object):
    pass


class CourseCommentAdmin(object):
    pass


class UserFavoriteAdmin(object):
    pass


class UserCourseAdmin(object):
    pass


class UserMessageAdmin(object):
    pass


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)