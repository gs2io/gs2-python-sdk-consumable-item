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

class Item(object):

    def __init__(self, params=None):
        if params is None:
            self.__item_id = None
            self.__create_at = None
            self.__name = None
            self.__max = None
            self.__item_pool_id = None
            self.__update_at = None
        else:
            self.set_item_id(params['itemId'] if 'itemId' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_max(params['max'] if 'max' in params.keys() else None)
            self.set_item_pool_id(params['itemPoolId'] if 'itemPoolId' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)


    def get_item_id(self):
        """
        消費型アイテムIDを取得
        :return: 消費型アイテムID
        :rtype: unicode
        """
        return self.__item_id

    def set_item_id(self, item_id):
        """
        消費型アイテムIDを設定
        :param item_id: 消費型アイテムID
        :type item_id: unicode
        """
        self.__item_id = item_id

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

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

    def get_max(self):
        """
        所持数の上限を取得
        :return: 所持数の上限
        :rtype: int
        """
        return self.__max

    def set_max(self, max):
        """
        所持数の上限を設定
        :param max: 所持数の上限
        :type max: int
        """
        self.__max = max

    def get_item_pool_id(self):
        """
        消費型アイテムプールIDを取得
        :return: 消費型アイテムプールID
        :rtype: unicode
        """
        return self.__item_pool_id

    def set_item_pool_id(self, item_pool_id):
        """
        消費型アイテムプールIDを設定
        :param item_pool_id: 消費型アイテムプールID
        :type item_pool_id: unicode
        """
        self.__item_pool_id = item_pool_id

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def to_dict(self):
        return { 
            "itemId": self.__item_id,
            "createAt": self.__create_at,
            "name": self.__name,
            "max": self.__max,
            "itemPoolId": self.__item_pool_id,
            "updateAt": self.__update_at,
        }