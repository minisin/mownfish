# -*- coding: utf-8 -*-
#
# This package will contain the handlers of your Tornado project


import statinfo_handler
import index_handler


ROUTES = {'mownfish': [(r'/statinfo', statinfo_handler.StatInfoHandler),
                       (r'/', index_handler.IndexHandler)]}
