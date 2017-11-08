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


class DeleteItemRequest(Gs2BasicRequest):

    class Constant(Gs2ConsumableItem):
        FUNCTION = "DeleteItem"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteItemRequest, self).__init__(params)
        if params is None:
            self.__item_pool_name = None
            self.__item_name = None
        else:
            self.set_item_pool_name(params['itemPoolName'] if 'itemPoolName' in params.keys() else None)
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)

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
        :rtype: DeleteItemRequest
        """
        self.set_item_pool_name(item_pool_name)
        return self

    def get_item_name(self):
        """
        消費型アイテムの名前を取得
        :return: 消費型アイテムの名前
        :rtype: unicode
        """
        return self.__item_name

    def set_item_name(self, item_name):
        """
        消費型アイテムの名前を設定
        :param item_name: 消費型アイテムの名前
        :type item_name: unicode
        """
        self.__item_name = item_name

    def with_item_name(self, item_name):
        """
        消費型アイテムの名前を設定
        :param item_name: 消費型アイテムの名前
        :type item_name: unicode
        :return: this
        :rtype: DeleteItemRequest
        """
        self.set_item_name(item_name)
        return self
