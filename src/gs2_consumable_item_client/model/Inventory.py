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

class Inventory(object):

    def __init__(self, params=None):
        if params is None:
            self.__count = None
            self.__create_at = None
            self.__item_name = None
            self.__inventory_id = None
            self.__user_id = None
            self.__update_at = None
        else:
            self.set_count(params['count'] if 'count' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)
            self.set_inventory_id(params['inventoryId'] if 'inventoryId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)


    def get_count(self):
        """
        所持数量を取得
        :return: 所持数量
        :rtype: int
        """
        return self.__count

    def set_count(self, count):
        """
        所持数量を設定
        :param count: 所持数量
        :type count: int
        """
        self.__count = count

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

    def get_item_name(self):
        """
        消費型アイテム名を取得
        :return: 消費型アイテム名
        :rtype: unicode
        """
        return self.__item_name

    def set_item_name(self, item_name):
        """
        消費型アイテム名を設定
        :param item_name: 消費型アイテム名
        :type item_name: unicode
        """
        self.__item_name = item_name

    def get_inventory_id(self):
        """
        所持品IDを取得
        :return: 所持品ID
        :rtype: unicode
        """
        return self.__inventory_id

    def set_inventory_id(self, inventory_id):
        """
        所持品IDを設定
        :param inventory_id: 所持品ID
        :type inventory_id: unicode
        """
        self.__inventory_id = inventory_id

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

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
            "count": self.__count,
            "createAt": self.__create_at,
            "itemName": self.__item_name,
            "inventoryId": self.__inventory_id,
            "userId": self.__user_id,
            "updateAt": self.__update_at,
        }