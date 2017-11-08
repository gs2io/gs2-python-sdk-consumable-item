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


class CreateItemRequest(Gs2BasicRequest):

    class Constant(Gs2ConsumableItem):
        FUNCTION = "CreateItem"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateItemRequest, self).__init__(params)
        if params is None:
            self.__item_pool_name = None
            self.__max = None
            self.__name = None
        else:
            self.set_item_pool_name(params['itemPoolName'] if 'itemPoolName' in params.keys() else None)
            self.set_max(params['max'] if 'max' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)

    def get_item_pool_name(self):
        """
        消費型アイテムプールの名前を取得
        :return: 消費型アイテムプールの名前
        :rtype: unicode
        """
        return self.__item_pool_name

    def set_item_pool_name(self, item_pool_name):
        """
        消費型アイテムプールの名前を設定
        :param item_pool_name: 消費型アイテムプールの名前
        :type item_pool_name: unicode
        """
        self.__item_pool_name = item_pool_name

    def with_item_pool_name(self, item_pool_name):
        """
        消費型アイテムプールの名前を設定
        :param item_pool_name: 消費型アイテムプールの名前
        :type item_pool_name: unicode
        :return: this
        :rtype: CreateItemRequest
        """
        self.set_item_pool_name(item_pool_name)
        return self

    def get_max(self):
        """
        最大所持数。を取得
        :return: 最大所持数。
        :rtype: int
        """
        return self.__max

    def set_max(self, max):
        """
        最大所持数。を設定
        :param max: 最大所持数。
        :type max: int
        """
        self.__max = max

    def with_max(self, max):
        """
        最大所持数。を設定
        :param max: 最大所持数。
        :type max: int
        :return: this
        :rtype: CreateItemRequest
        """
        self.set_max(max)
        return self

    def get_name(self):
        """
        消費型アイテム名を取得
        :return: 消費型アイテム名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        消費型アイテム名を設定
        :param name: 消費型アイテム名
        :type name: unicode
        """
        self.__name = name

    def with_name(self, name):
        """
        消費型アイテム名を設定
        :param name: 消費型アイテム名
        :type name: unicode
        :return: this
        :rtype: CreateItemRequest
        """
        self.set_name(name)
        return self
