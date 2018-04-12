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


class UpdateItemRequest(Gs2BasicRequest):

    class Constant(Gs2ConsumableItem):
        FUNCTION = "UpdateItem"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(UpdateItemRequest, self).__init__(params)
        if params is None:
            self.__item_pool_name = None
        else:
            self.set_item_pool_name(params['itemPoolName'] if 'itemPoolName' in params.keys() else None)
        if params is None:
            self.__item_name = None
        else:
            self.set_item_name(params['itemName'] if 'itemName' in params.keys() else None)
        if params is None:
            self.__max = None
        else:
            self.set_max(params['max'] if 'max' in params.keys() else None)
        if params is None:
            self.__acquisition_inventory_trigger_script = None
        else:
            self.set_acquisition_inventory_trigger_script(params['acquisitionInventoryTriggerScript'] if 'acquisitionInventoryTriggerScript' in params.keys() else None)
        if params is None:
            self.__acquisition_inventory_done_trigger_script = None
        else:
            self.set_acquisition_inventory_done_trigger_script(params['acquisitionInventoryDoneTriggerScript'] if 'acquisitionInventoryDoneTriggerScript' in params.keys() else None)
        if params is None:
            self.__consume_inventory_trigger_script = None
        else:
            self.set_consume_inventory_trigger_script(params['consumeInventoryTriggerScript'] if 'consumeInventoryTriggerScript' in params.keys() else None)
        if params is None:
            self.__consume_inventory_done_trigger_script = None
        else:
            self.set_consume_inventory_done_trigger_script(params['consumeInventoryDoneTriggerScript'] if 'consumeInventoryDoneTriggerScript' in params.keys() else None)

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
        if not isinstance(item_pool_name, unicode):
            raise TypeError(type(item_pool_name))
        self.__item_pool_name = item_pool_name

    def with_item_pool_name(self, item_pool_name):
        """
        消費型アイテムプールの名前を設定
        :param item_pool_name: 消費型アイテムプールの名前
        :type item_pool_name: unicode
        :return: this
        :rtype: UpdateItemRequest
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
        if not isinstance(item_name, unicode):
            raise TypeError(type(item_name))
        self.__item_name = item_name

    def with_item_name(self, item_name):
        """
        消費型アイテムの名前を設定
        :param item_name: 消費型アイテムの名前
        :type item_name: unicode
        :return: this
        :rtype: UpdateItemRequest
        """
        self.set_item_name(item_name)
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
        if not isinstance(max, int):
            raise TypeError(type(max))
        self.__max = max

    def with_max(self, max):
        """
        最大所持数。を設定
        :param max: 最大所持数。
        :type max: int
        :return: this
        :rtype: UpdateItemRequest
        """
        self.set_max(max)
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
        if not isinstance(acquisition_inventory_trigger_script, unicode):
            raise TypeError(type(acquisition_inventory_trigger_script))
        self.__acquisition_inventory_trigger_script = acquisition_inventory_trigger_script

    def with_acquisition_inventory_trigger_script(self, acquisition_inventory_trigger_script):
        """
        アイテム入手時 に実行されるGS2-Scriptを設定
        :param acquisition_inventory_trigger_script: アイテム入手時 に実行されるGS2-Script
        :type acquisition_inventory_trigger_script: unicode
        :return: this
        :rtype: UpdateItemRequest
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
        if not isinstance(acquisition_inventory_done_trigger_script, unicode):
            raise TypeError(type(acquisition_inventory_done_trigger_script))
        self.__acquisition_inventory_done_trigger_script = acquisition_inventory_done_trigger_script

    def with_acquisition_inventory_done_trigger_script(self, acquisition_inventory_done_trigger_script):
        """
        アイテム入手完了時 に実行されるGS2-Scriptを設定
        :param acquisition_inventory_done_trigger_script: アイテム入手完了時 に実行されるGS2-Script
        :type acquisition_inventory_done_trigger_script: unicode
        :return: this
        :rtype: UpdateItemRequest
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
        if not isinstance(consume_inventory_trigger_script, unicode):
            raise TypeError(type(consume_inventory_trigger_script))
        self.__consume_inventory_trigger_script = consume_inventory_trigger_script

    def with_consume_inventory_trigger_script(self, consume_inventory_trigger_script):
        """
        アイテム消費時 に実行されるGS2-Scriptを設定
        :param consume_inventory_trigger_script: アイテム消費時 に実行されるGS2-Script
        :type consume_inventory_trigger_script: unicode
        :return: this
        :rtype: UpdateItemRequest
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
        if not isinstance(consume_inventory_done_trigger_script, unicode):
            raise TypeError(type(consume_inventory_done_trigger_script))
        self.__consume_inventory_done_trigger_script = consume_inventory_done_trigger_script

    def with_consume_inventory_done_trigger_script(self, consume_inventory_done_trigger_script):
        """
        アイテム消費完了時 に実行されるGS2-Scriptを設定
        :param consume_inventory_done_trigger_script: アイテム消費完了時 に実行されるGS2-Script
        :type consume_inventory_done_trigger_script: unicode
        :return: this
        :rtype: UpdateItemRequest
        """
        self.set_consume_inventory_done_trigger_script(consume_inventory_done_trigger_script)
        return self
