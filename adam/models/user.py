# -*- coding: utf-8 -*-
from oodo import api,fields,models

class AdamUser(models.Model):
    _name = "adam.user"

    name = fields.Char('姓名')
    phone = fields.Char('电话')
