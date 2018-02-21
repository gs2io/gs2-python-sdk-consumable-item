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


class UpdateItemPoolRequest(Gs2BasicRequest):

    class Constant(Gs2ConsumableItem):
        FUNCTION = "UpdateItemPool"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateItemPoolRequest, self).__init__(params)
        if params is None:
            self.__item_pool_name = None
            self.__description = None
            self.__service_class = None
            self.__acquisition_inventory_trigger_script = None
            self.__acquisition_inventory_done_trigger_script = None
            self.__consume_inventory_trigger_script = None
            self.__consume_inventory_done_trigger_script = None
        else:
            self.set_item_pool_name(params['itemPoolName'] if 'itemPoolName' in params.keys() else None)
            self.set_description(params['description'] if 'description' in params.keys() else None)
            self.set_service_class(params['serviceClass'] if 'serviceClass' in params.keys() else None)
            self.set_acquisition_inventory_trigger_script(params['acquisitionInventoryTriggerScript'] if 'acquisitionInventoryTriggerScript' in params.keys() else None)
            self.set_acquisition_inventory_done_trigger_script(params['acquisitionInventoryDoneTriggerScript'] if 'acquisitionInventoryDoneTriggerScript' in params.keys() else None)
            self.set_consume_inventory_trigger_script(params['consumeInventoryTriggerScript'] if 'consumeInventoryTriggerScript' in params.keys() else None)
            self.set_consume_inventory_done_trigger_script(params['consumeInventoryDoneTriggerScript'] if 'consumeInventoryDoneTriggerScript' in params.keys() else None)

    def get_item_pool_name(self):
        """
        更新する消費型アイテムプールの名前を取得
        :return: 更新する消費型アイテムプールの名前
        :rtype: unicode
        """
        return self.__item_pool_name

    def set_item_pool_name(self, item_pool_name):
        """
        更新する消費型アイテムプールの名前を設定
        :param item_pool_name: 更新する消費型アイテムプールの名前
        :type item_pool_name: unicode
        """
        self.__item_pool_name = item_pool_name

    def with_item_pool_name(self, item_pool_name):
        """
        更新する消費型アイテムプールの名前を設定
        :param item_pool_name: 更新する消費型アイテムプールの名前
        :type item_pool_name: unicode
        :return: this
        :rtype: UpdateItemPoolRequest
        """
        self.set_item_pool_name(item_pool_name)
        return self

    def get_description(self):
        """
        説明文(1024文字以内)を取得
        :return: 説明文(1024文字以内)
        :rtype: unicode
        """
        return self.__description

    def set_description(self, description):
        """
        説明文(1024文字以内)を設定
        :param description: 説明文(1024文字以内)
        :type description: unicode
        """
        self.__description = description

    def with_description(self, description):
        """
        説明文(1024文字以内)を設定
        :param description: 説明文(1024文字以内)
        :type description: unicode
        :return: this
        :rtype: UpdateItemPoolRequest
        """
        self.set_description(description)
        return self

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

    def with_service_class(self, service_class):
        """
        サービスクラスを設定
        :param service_class: サービスクラス
        :type service_class: unicode
        :return: this
        :rtype: UpdateItemPoolRequest
        """
        self.set_service_class(service_class)
        return self

    def get_acquisition_inventory_trigger_script(self):
        """
        アイテム入手時 に実行されるGS2-Scriptを取得
        :return: アイテム入手時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__acquisition_inventory_trigger_script

    def set_acquisition_inventory_trigger_script(self, acquisition_inventory_trigger_script):
        """
        アイテム入手時 に実行されるGS2-Scriptを設定
        :param acquisition_inventory_trigger_script: アイテム入手時 に実行されるGS2-Script
        :type acquisition_inventory_trigger_script: unicode
        """
        self.__acquisition_inventory_trigger_script = acquisition_inventory_trigger_script

    def with_acquisition_inventory_trigger_script(self, acquisition_inventory_trigger_script):
        """
        アイテム入手時 に実行されるGS2-Scriptを設定
        :param acquisition_inventory_trigger_script: アイテム入手時 に実行されるGS2-Script
        :type acquisition_inventory_trigger_script: unicode
        :return: this
        :rtype: UpdateItemPoolRequest
        """
        self.set_acquisition_inventory_trigger_script(acquisition_inventory_trigger_script)
        return self

    def get_acquisition_inventory_done_trigger_script(self):
        """
        アイテム入手完了時 に実行されるGS2-Scriptを取得
        :return: アイテム入手完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__acquisition_inventory_done_trigger_script

    def set_acquisition_inventory_done_trigger_script(self, acquisition_inventory_done_trigger_script):
        """
        アイテム入手完了時 に実行されるGS2-Scriptを設定
        :param acquisition_inventory_done_trigger_script: アイテム入手完了時 に実行されるGS2-Script
        :type acquisition_inventory_done_trigger_script: unicode
        """
        self.__acquisition_inventory_done_trigger_script = acquisition_inventory_done_trigger_script

    def with_acquisition_inventory_done_trigger_script(self, acquisition_inventory_done_trigger_script):
        """
        アイテム入手完了時 に実行されるGS2-Scriptを設定
        :param acquisition_inventory_done_trigger_script: アイテム入手完了時 に実行されるGS2-Script
        :type acquisition_inventory_done_trigger_script: unicode
        :return: this
        :rtype: UpdateItemPoolRequest
        """
        self.set_acquisition_inventory_done_trigger_script(acquisition_inventory_done_trigger_script)
        return self

    def get_consume_inventory_trigger_script(self):
        """
        アイテム消費時 に実行されるGS2-Scriptを取得
        :return: アイテム消費時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_inventory_trigger_script

    def set_consume_inventory_trigger_script(self, consume_inventory_trigger_script):
        """
        アイテム消費時 に実行されるGS2-Scriptを設定
        :param consume_inventory_trigger_script: アイテム消費時 に実行されるGS2-Script
        :type consume_inventory_trigger_script: unicode
        """
        self.__consume_inventory_trigger_script = consume_inventory_trigger_script

    def with_consume_inventory_trigger_script(self, consume_inventory_trigger_script):
        """
        アイテム消費時 に実行されるGS2-Scriptを設定
        :param consume_inventory_trigger_script: アイテム消費時 に実行されるGS2-Script
        :type consume_inventory_trigger_script: unicode
        :return: this
        :rtype: UpdateItemPoolRequest
        """
        self.set_consume_inventory_trigger_script(consume_inventory_trigger_script)
        return self

    def get_consume_inventory_done_trigger_script(self):
        """
        アイテム消費完了時 に実行されるGS2-Scriptを取得
        :return: アイテム消費完了時 に実行されるGS2-Script
        :rtype: unicode
        """
        return self.__consume_inventory_done_trigger_script

    def set_consume_inventory_done_trigger_script(self, consume_inventory_done_trigger_script):
        """
        アイテム消費完了時 に実行されるGS2-Scriptを設定
        :param consume_inventory_done_trigger_script: アイテム消費完了時 に実行されるGS2-Script
        :type consume_inventory_done_trigger_script: unicode
        """
        self.__consume_inventory_done_trigger_script = consume_inventory_done_trigger_script

    def with_consume_inventory_done_trigger_script(self, consume_inventory_done_trigger_script):
        """
        アイテム消費完了時 に実行されるGS2-Scriptを設定
        :param consume_inventory_done_trigger_script: アイテム消費完了時 に実行されるGS2-Script
        :type consume_inventory_done_trigger_script: unicode
        :return: this
        :rtype: UpdateItemPoolRequest
        """
        self.set_consume_inventory_done_trigger_script(consume_inventory_done_trigger_script)
        return self
