# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModMY6Vhyqk", version="0.0.1")
class Script_NeteaseModMY6Vhyqk(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModMY6VhyqkServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModMY6VhyqkServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModMY6VhyqkClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModMY6VhyqkClientDestroy(self):
        pass
