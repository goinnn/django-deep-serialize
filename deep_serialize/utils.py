# -*- coding: utf-8 -*-
# Copyright (c) 2013 by Pablo Martín <goinnn@gmail.com>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.
import json

from django.core.serializers.json import DjangoJSONEncoder


def has_natural_key(content):
    model = content.__class__
    return getattr(content, 'natural_key', None) and getattr(model.objects, 'get_by_natural_key', None)


def dumps(fixtures_python):
    return json.dumps(fixtures_python, cls=DjangoJSONEncoder, sort_keys=True)
