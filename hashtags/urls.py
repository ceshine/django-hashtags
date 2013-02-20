# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 Guilherme Gondim and contributors
#
# This file is part of Django Hashtags.
#
# Django Hashtags is free software under terms of the GNU Lesser
# General Public License version 3 (LGPLv3) as published by the Free
# Software Foundation. See the file README for copying conditions.

from django.conf.urls.defaults import *
from hashtags.models import Hashtag
from hashtags.views import hashtag_index, hashtagged_item_list

index_url = url(
    regex  = '^$',
    view   = hashtag_index,
    name   = 'hashtag_index',
)

hashtagged_item_list_url = url(
    regex  = '^(?P<hashtag>[-\w]+)/$',
    view   = hashtagged_item_list,
    kwargs = {'paginate_by': 10},
    name   = 'hashtagged_item_list',
)

hashtagged_item_list_url_paginated = url(
    regex  = '^(?P<hashtag>[-\w]+)/(?P<page>[1-9][0-9]*)/$',
    view   = hashtagged_item_list,
    kwargs = {'paginate_by': 10},
    name   = 'hashtagged_item_list_pagenated',
)

urlpatterns = patterns('', index_url, hashtagged_item_list_url, hashtagged_item_list_url_paginated)
