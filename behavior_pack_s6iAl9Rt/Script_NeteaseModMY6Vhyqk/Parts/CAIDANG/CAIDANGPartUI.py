# -*- coding: utf-8 -*-
# created by chenzhikun at 2021/09/17
# contact: chenzhikun@corp.netease.com
from Preset.Model.Blueprint.BaseUIBlueprintScreen import BaseUIBlueprintScreen
from Preset.Model.GameObject import registerGenericClass


@registerGenericClass('CAIDANGPartUIScreen')
class CAIDANGPartUIScreen(BaseUIBlueprintScreen):
	def __init__(self, namespace, name, param=None):
		super(CAIDANGPartUIScreen, self).__init__(namespace, name, param)
