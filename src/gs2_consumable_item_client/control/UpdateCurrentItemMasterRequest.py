# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_consumable_item_client.Gs2ConsumableItem import Gs2ConsumableItem


class UpdateCurrentItemMasterRequest(Gs2BasicRequest):

    class Constant(Gs2ConsumableItem):
        FUNCTION = "UpdateCurrentItemMaster"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateCurrentItemMasterRequest, self).__init__(params)
        if params is None:
            self.__item_pool_name = None
        else:
            self.set_item_pool_name(params['itemPoolName'] if 'itemPoolName' in params.keys() else None)
        if params is None:
            self.__settings = None
        else:
            self.set_settings(params['settings'] if 'settings' in params.keys() else None)

    def get_item_pool_name(self):
        """
        アイテムプールの名前を指定します。を取得
        :return: アイテムプールの名前を指定します。
        :rtype: unicode
        """
        return self.__item_pool_name

    def set_item_pool_name(self, item_pool_name):
        """
        アイテムプールの名前を指定します。を設定
        :param item_pool_name: アイテムプールの名前を指定します。
        :type item_pool_name: unicode
        """
        if item_pool_name and not (isinstance(item_pool_name, str) or isinstance(item_pool_name, unicode)):
            raise TypeError(type(item_pool_name))
        self.__item_pool_name = item_pool_name

    def with_item_pool_name(self, item_pool_name):
        """
        アイテムプールの名前を指定します。を設定
        :param item_pool_name: アイテムプールの名前を指定します。
        :type item_pool_name: unicode
        :return: this
        :rtype: UpdateCurrentItemMasterRequest
        """
        self.set_item_pool_name(item_pool_name)
        return self

    def get_settings(self):
        """
        アイテムマスターデータを取得
        :return: アイテムマスターデータ
        :rtype: unicode
        """
        return self.__settings

    def set_settings(self, settings):
        """
        アイテムマスターデータを設定
        :param settings: アイテムマスターデータ
        :type settings: unicode
        """
        if settings and not (isinstance(settings, str) or isinstance(settings, unicode)):
            raise TypeError(type(settings))
        self.__settings = settings

    def with_settings(self, settings):
        """
        アイテムマスターデータを設定
        :param settings: アイテムマスターデータ
        :type settings: unicode
        :return: this
        :rtype: UpdateCurrentItemMasterRequest
        """
        self.set_settings(settings)
        return self
