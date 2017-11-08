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

class ItemPool(object):

    def __init__(self, params=None):
        if params is None:
            self.__create_at = None
            self.__name = None
            self.__owner_id = None
            self.__item_pool_id = None
            self.__service_class = None
            self.__update_at = None
            self.__description = None
        else:
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_item_pool_id(params['itemPoolId'] if 'itemPoolId' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)


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
        消費型アイテムプール名を取得
        :return: 消費型アイテムプール名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        消費型アイテムプール名を設定
        :param name: 消費型アイテムプール名
        :type name: unicode
        """
        self.__name = name

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

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

    def get_service_class(self):
        """
        サービスクラスを取得
        :return: サービスクラス
        :rtype: unicode
        """
        return self.__service_class

    def set_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        """
        self.__service_class = service_class

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

    def get_description(self):
        """
        説明文を取得
        :return: 説明文
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文を設定
        :param description: 説明文
        :type description: unicode
        """
        self.__description = description

    def to_dict(self):
        return { 
            "createAt": self.__create_at,
            "name": self.__name,
            "ownerId": self.__owner_id,
            "itemPoolId": self.__item_pool_id,
            "serviceClass": self.__service_class,
            "updateAt": self.__update_at,
            "description": self.__description,
        }