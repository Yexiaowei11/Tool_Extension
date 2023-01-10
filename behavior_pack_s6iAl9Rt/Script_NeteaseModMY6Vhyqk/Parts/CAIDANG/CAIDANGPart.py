# -*- coding: utf-8 -*-

from Preset.Model.Blueprint.BaseUIBlueprintPart import BaseUIBlueprintPart
from Preset.Model.GameObject import registerGenericClass


@registerGenericClass('CAIDANGPart')
class CAIDANGPart(BaseUIBlueprintPart):

    def __init__(self):
        super(CAIDANGPart, self).__init__()
        self.name = 'UI蓝图零件'
        self.description = '蓝图UI零件'
        self.bpFiles = ['CAIDANGPart.bp']
        self.etsFiles = ['']
