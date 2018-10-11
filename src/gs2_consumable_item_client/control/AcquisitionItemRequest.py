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

from gs2_core_client.Gs2UserRequest import Gs2UserRequest
from gs2_consumable_item_client.Gs2ConsumableItem import Gs2ConsumableItem


class AcquisitionItemRequest(Gs2UserRequest):

    class Constant(Gs2ConsumableItem):
        FUNCTION = "AcquisitionItem"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(AcquisitionItemRequest, self).__init__(params)
        if params is None:
            self.__item_pool_name = None
            self.__item_name = None
            self.__count = None
            self.__expire_at = None
        else:
            self.set_item_pool_name(params['itemPoolName'] if 'itemPoolName' in params.keys() else None)
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)
            self.set_count(params['count'] if 'count' in params.keys() else None)
            self.set_expire_at(params['expireAt'] if 'expireAt' in params.keys() else None)

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
        if item_pool_name is not None and not (isinstance(item_pool_name, str) or isinstance(item_pool_name, unicode)):
            raise TypeError(type(item_pool_name))
        self.__item_pool_name = item_pool_name

    def with_item_pool_name(self, item_pool_name):
        """
        消費型アイテムプールの名前を設定
        :param item_pool_name: 消費型アイテムプールの名前
        :type item_pool_name: unicode
        :return: this
        :rtype: AcquisitionItemRequest
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
        if item_name is not None and not (isinstance(item_name, str) or isinstance(item_name, unicode)):
            raise TypeError(type(item_name))
        self.__item_name = item_name

    def with_item_name(self, item_name):
        """
        消費型アイテムの名前を設定
        :param item_name: 消費型アイテムの名前
        :type item_name: unicode
        :return: this
        :rtype: AcquisitionItemRequest
        """
        self.set_item_name(item_name)
        return self

    def get_count(self):
        """
        入手数量を取得
        :return: 入手数量
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        入手数量を設定
        :param count: 入手数量
        :type count: int
        """
        if count is not None and not isinstance(count, int):
            raise TypeError(type(count))
        self.__count = count

    def with_count(self, count):
        """
        入手数量を設定
        :param count: 入手数量
        :type count: int
        :return: this
        :rtype: AcquisitionItemRequest
        """
        self.set_count(count)
        return self

    def get_expire_at(self):
        """
        有効期限(エポック秒)を取得
        :return: 有効期限(エポック秒)
        :rtype: int
        """
        return self.__expire_at

    def set_expire_at(self, expire_at):
        """
        有効期限(エポック秒)を設定
        :param expire_at: 有効期限(エポック秒)
        :type expire_at: int
        """
        if expire_at is not None and not isinstance(expire_at, int):
            raise TypeError(type(expire_at))
        self.__expire_at = expire_at

    def with_expire_at(self, expire_at):
        """
        有効期限(エポック秒)を設定
        :param expire_at: 有効期限(エポック秒)
        :type expire_at: int
        :return: this
        :rtype: AcquisitionItemRequest
        """
        self.set_expire_at(expire_at)
        return self
