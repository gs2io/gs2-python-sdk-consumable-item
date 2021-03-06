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
            self.__item_pool_id = None
            self.__owner_id = None
            self.__name = None
            self.__description = None
            self.__service_class = None
            self.__acquisition_item_trigger_script = None
            self.__acquisition_item_done_trigger_script = None
            self.__consume_item_trigger_script = None
            self.__consume_item_done_trigger_script = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_item_pool_id(params['itemPoolId'] if 'itemPoolId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_acquisition_item_trigger_script(params['acquisitionItemTriggerScript'] if 'acquisitionItemTriggerScript' in params.keys() else None)
            self.set_acquisition_item_done_trigger_script(params['acquisitionItemDoneTriggerScript'] if 'acquisitionItemDoneTriggerScript' in params.keys() else None)
            self.set_consume_item_trigger_script(params['consumeItemTriggerScript'] if 'consumeItemTriggerScript' in params.keys() else None)
            self.set_consume_item_done_trigger_script(params['consumeItemDoneTriggerScript'] if 'consumeItemDoneTriggerScript' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

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

    def get_acquisition_item_trigger_script(self):
        """
        アイテム入手時 に実行されるGS2-Scriptを取得
        :return: アイテム入手時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__acquisition_item_trigger_script

    def set_acquisition_item_trigger_script(self, acquisition_item_trigger_script):
        """
        アイテム入手時 に実行されるGS2-Scriptを設定
        :param acquisition_item_trigger_script: アイテム入手時 に実行されるGS2-Script
        :type acquisition_item_trigger_script: unicode
        """
        self.__acquisition_item_trigger_script = acquisition_item_trigger_script

    def get_acquisition_item_done_trigger_script(self):
        """
        アイテム入手完了時 に実行されるGS2-Scriptを取得
        :return: アイテム入手完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__acquisition_item_done_trigger_script

    def set_acquisition_item_done_trigger_script(self, acquisition_item_done_trigger_script):
        """
        アイテム入手完了時 に実行されるGS2-Scriptを設定
        :param acquisition_item_done_trigger_script: アイテム入手完了時 に実行されるGS2-Script
        :type acquisition_item_done_trigger_script: unicode
        """
        self.__acquisition_item_done_trigger_script = acquisition_item_done_trigger_script

    def get_consume_item_trigger_script(self):
        """
        アイテム消費時 に実行されるGS2-Scriptを取得
        :return: アイテム消費時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_item_trigger_script

    def set_consume_item_trigger_script(self, consume_item_trigger_script):
        """
        アイテム消費時 に実行されるGS2-Scriptを設定
        :param consume_item_trigger_script: アイテム消費時 に実行されるGS2-Script
        :type consume_item_trigger_script: unicode
        """
        self.__consume_item_trigger_script = consume_item_trigger_script

    def get_consume_item_done_trigger_script(self):
        """
        アイテム消費完了時 に実行されるGS2-Scriptを取得
        :return: アイテム消費完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_item_done_trigger_script

    def set_consume_item_done_trigger_script(self, consume_item_done_trigger_script):
        """
        アイテム消費完了時 に実行されるGS2-Scriptを設定
        :param consume_item_done_trigger_script: アイテム消費完了時 に実行されるGS2-Script
        :type consume_item_done_trigger_script: unicode
        """
        self.__consume_item_done_trigger_script = consume_item_done_trigger_script

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

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(ItemPool, self).__getitem__(key)

    def to_dict(self):
        return {
            "itemPoolId": self.__item_pool_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "description": self.__description,
            "serviceClass": self.__service_class,
            "acquisitionItemTriggerScript": self.__acquisition_item_trigger_script,
            "acquisitionItemDoneTriggerScript": self.__acquisition_item_done_trigger_script,
            "consumeItemTriggerScript": self.__consume_item_trigger_script,
            "consumeItemDoneTriggerScript": self.__consume_item_done_trigger_script,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
