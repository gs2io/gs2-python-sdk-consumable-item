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

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client
from aws_sdk_for_serverless.common import url_encoder


class Gs2ConsumableItemClient(AbstractGs2Client):

    ENDPOINT = "consumable-item"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2ConsumableItemClient, self).__init__(credential, region)

    def get_current_item_master(self, request):
        """
        公開されているアイテムマスタを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetCurrentItemMasterRequest.GetCurrentItemMasterRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetCurrentItemMasterResult.GetCurrentItemMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetCurrentItemMasterRequest import GetCurrentItemMasterRequest

        from gs2_consumable_item_client.control.GetCurrentItemMasterResult import GetCurrentItemMasterResult
        return GetCurrentItemMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/master",
            service=self.ENDPOINT,
            component=GetCurrentItemMasterRequest.Constant.MODULE,
            target_function=GetCurrentItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_current_item_master(self, request):
        """
        公開するアイテムマスタを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.UpdateCurrentItemMasterRequest.UpdateCurrentItemMasterRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.UpdateCurrentItemMasterResult.UpdateCurrentItemMasterResult
        """
        body = { 
            "settings": request.get_settings(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.UpdateCurrentItemMasterRequest import UpdateCurrentItemMasterRequest
        from gs2_consumable_item_client.control.UpdateCurrentItemMasterResult import UpdateCurrentItemMasterResult
        return UpdateCurrentItemMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/master",
            service=self.ENDPOINT,
            component=UpdateCurrentItemMasterRequest.Constant.MODULE,
            target_function=UpdateCurrentItemMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def acquisition_item(self, request):
        """
        インベントリにアイテムを加えます<br>
        <br>
        アイテムに所持数の上限が設定されている状態で、複数個付与することによって<br>
        所持数の上限を超えてしまうケースでは一切付与せずエラー応答を返します。<br>
        <br>
        例えば、所持数上限 10 のアイテムで、8個所持しているユーザに 3個 付与しようとすると<br>
        1個も付与せずにエラーを返します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.AcquisitionItemRequest.AcquisitionItemRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.AcquisitionItemResult.AcquisitionItemResult
        """
        body = { 
            "count": request.get_count(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.AcquisitionItemRequest import AcquisitionItemRequest
        from gs2_consumable_item_client.control.AcquisitionItemResult import AcquisitionItemResult
        return AcquisitionItemResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/my/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=AcquisitionItemRequest.Constant.MODULE,
            target_function=AcquisitionItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def acquisition_item_by_stamp_sheet(self, request):
        """
        スタンプシートを使用してインベントリにアイテムを加えます<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.AcquisitionItemByStampSheetRequest.AcquisitionItemByStampSheetRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.AcquisitionItemByStampSheetResult.AcquisitionItemByStampSheetResult
        """
        body = { 
            "sheet": request.get_sheet(),
            "keyName": request.get_key_name(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.AcquisitionItemByStampSheetRequest import AcquisitionItemByStampSheetRequest
        from gs2_consumable_item_client.control.AcquisitionItemByStampSheetResult import AcquisitionItemByStampSheetResult
        return AcquisitionItemByStampSheetResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inventory",
            service=self.ENDPOINT,
            component=AcquisitionItemByStampSheetRequest.Constant.MODULE,
            target_function=AcquisitionItemByStampSheetRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def acquisition_item_by_user_id(self, request):
        """
        インベントリにアイテムを加えます<br>
        <br>
        アイテムに所持数の上限が設定されている状態で、複数個付与することによって<br>
        所持数の上限を超えてしまうケースでは一切付与せずエラー応答を返します。<br>
        <br>
        例えば、所持数上限 10 のアイテムで、8個所持しているユーザに 3個 付与しようとすると<br>
        1個も付与せずにエラーを返します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.AcquisitionItemByUserIdRequest.AcquisitionItemByUserIdRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.AcquisitionItemByUserIdResult.AcquisitionItemByUserIdResult
        """
        body = { 
            "count": request.get_count(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.AcquisitionItemByUserIdRequest import AcquisitionItemByUserIdRequest
        from gs2_consumable_item_client.control.AcquisitionItemByUserIdResult import AcquisitionItemByUserIdResult
        return AcquisitionItemByUserIdResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=AcquisitionItemByUserIdRequest.Constant.MODULE,
            target_function=AcquisitionItemByUserIdRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def consume_item(self, request):
        """
        インベントリのアイテムを消費します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.ConsumeItemRequest.ConsumeItemRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.ConsumeItemResult.ConsumeItemResult
        """
        body = { 
            "count": request.get_count(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.ConsumeItemRequest import ConsumeItemRequest
        from gs2_consumable_item_client.control.ConsumeItemResult import ConsumeItemResult
        return ConsumeItemResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/my/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=ConsumeItemRequest.Constant.MODULE,
            target_function=ConsumeItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def consume_item_by_stamp_task(self, request):
        """
        スタンプタスクを使用してインベントリのアイテムを消費します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.ConsumeItemByStampTaskRequest.ConsumeItemByStampTaskRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.ConsumeItemByStampTaskResult.ConsumeItemByStampTaskResult
        """
        body = { 
            "task": request.get_task(),
            "keyName": request.get_key_name(),
            "transactionId": request.get_transaction_id(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.ConsumeItemByStampTaskRequest import ConsumeItemByStampTaskRequest
        from gs2_consumable_item_client.control.ConsumeItemByStampTaskResult import ConsumeItemByStampTaskResult
        return ConsumeItemByStampTaskResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/inventory",
            service=self.ENDPOINT,
            component=ConsumeItemByStampTaskRequest.Constant.MODULE,
            target_function=ConsumeItemByStampTaskRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def consume_item_by_user_id(self, request):
        """
        インベントリのアイテムを消費します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.ConsumeItemByUserIdRequest.ConsumeItemByUserIdRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.ConsumeItemByUserIdResult.ConsumeItemByUserIdResult
        """
        body = { 
            "count": request.get_count(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.ConsumeItemByUserIdRequest import ConsumeItemByUserIdRequest
        from gs2_consumable_item_client.control.ConsumeItemByUserIdResult import ConsumeItemByUserIdResult
        return ConsumeItemByUserIdResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=ConsumeItemByUserIdRequest.Constant.MODULE,
            target_function=ConsumeItemByUserIdRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_inventory_by_user_id(self, request):
        """
        インベントリからアイテムを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DeleteInventoryByUserIdRequest.DeleteInventoryByUserIdRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DeleteInventoryByUserIdRequest import DeleteInventoryByUserIdRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteInventoryByUserIdRequest.Constant.MODULE,
            target_function=DeleteInventoryByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_inventory(self, request):
        """
        ユーザが所持しているインベントリの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DescribeInventoryRequest.DescribeInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.DescribeInventoryResult.DescribeInventoryResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DescribeInventoryRequest import DescribeInventoryRequest

        from gs2_consumable_item_client.control.DescribeInventoryResult import DescribeInventoryResult
        return DescribeInventoryResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/my",
            service=self.ENDPOINT,
            component=DescribeInventoryRequest.Constant.MODULE,
            target_function=DescribeInventoryRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_inventory_by_user_id(self, request):
        """
        ユーザが所持しているインベントリの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DescribeInventoryByUserIdRequest.DescribeInventoryByUserIdRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.DescribeInventoryByUserIdResult.DescribeInventoryByUserIdResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DescribeInventoryByUserIdRequest import DescribeInventoryByUserIdRequest

        from gs2_consumable_item_client.control.DescribeInventoryByUserIdResult import DescribeInventoryByUserIdResult
        return DescribeInventoryByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "",
            service=self.ENDPOINT,
            component=DescribeInventoryByUserIdRequest.Constant.MODULE,
            target_function=DescribeInventoryByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_inventory(self, request):
        """
        インベントリの内容を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetInventoryRequest.GetInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetInventoryResult.GetInventoryResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetInventoryRequest import GetInventoryRequest

        from gs2_consumable_item_client.control.GetInventoryResult import GetInventoryResult
        return GetInventoryResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/my/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=GetInventoryRequest.Constant.MODULE,
            target_function=GetInventoryRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_inventory_by_user_id(self, request):
        """
        インベントリの内容を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetInventoryByUserIdRequest.GetInventoryByUserIdRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetInventoryByUserIdResult.GetInventoryByUserIdResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetInventoryByUserIdRequest import GetInventoryByUserIdRequest

        from gs2_consumable_item_client.control.GetInventoryByUserIdResult import GetInventoryByUserIdResult
        return GetInventoryByUserIdResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/inventory/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=GetInventoryByUserIdRequest.Constant.MODULE,
            target_function=GetInventoryByUserIdRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def create_item_master(self, request):
        """
        消費型アイテムを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.CreateItemMasterRequest.CreateItemMasterRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.CreateItemMasterResult.CreateItemMasterResult
        """
        body = { 
            "name": request.get_name(),
        }

        if request.get_max() is not None:
            body["max"] = request.get_max()
        if request.get_acquisition_item_trigger_script() is not None:
            body["acquisitionItemTriggerScript"] = request.get_acquisition_item_trigger_script()
        if request.get_acquisition_item_done_trigger_script() is not None:
            body["acquisitionItemDoneTriggerScript"] = request.get_acquisition_item_done_trigger_script()
        if request.get_consume_item_trigger_script() is not None:
            body["consumeItemTriggerScript"] = request.get_consume_item_trigger_script()
        if request.get_consume_item_done_trigger_script() is not None:
            body["consumeItemDoneTriggerScript"] = request.get_consume_item_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.CreateItemMasterRequest import CreateItemMasterRequest
        from gs2_consumable_item_client.control.CreateItemMasterResult import CreateItemMasterResult
        return CreateItemMasterResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/master/item",
            service=self.ENDPOINT,
            component=CreateItemMasterRequest.Constant.MODULE,
            target_function=CreateItemMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_item_master(self, request):
        """
        消費型アイテムを削除します<br>
        <br>
        既にアイテムを所持しているユーザがいる場合、そのアイテムはインベントリから削除されることはありません。<br>
        消費型アイテムを削除することで新しくアイテムを付与することはできなくなりますが、消費することは出来ます。<br>
        <br>
        これを防ぎたい場合はすべてのユーザのインベントリを走査して該当アイテムを削除する必要があります。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DeleteItemMasterRequest.DeleteItemMasterRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DeleteItemMasterRequest import DeleteItemMasterRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/master/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteItemMasterRequest.Constant.MODULE,
            target_function=DeleteItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_item_master(self, request):
        """
        消費型アイテムの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DescribeItemMasterRequest.DescribeItemMasterRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.DescribeItemMasterResult.DescribeItemMasterResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DescribeItemMasterRequest import DescribeItemMasterRequest

        from gs2_consumable_item_client.control.DescribeItemMasterResult import DescribeItemMasterResult
        return DescribeItemMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/master/item",
            service=self.ENDPOINT,
            component=DescribeItemMasterRequest.Constant.MODULE,
            target_function=DescribeItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_item_master(self, request):
        """
        消費型アイテムを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetItemMasterRequest.GetItemMasterRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetItemMasterResult.GetItemMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetItemMasterRequest import GetItemMasterRequest

        from gs2_consumable_item_client.control.GetItemMasterResult import GetItemMasterResult
        return GetItemMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/master/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=GetItemMasterRequest.Constant.MODULE,
            target_function=GetItemMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_item_master(self, request):
        """
        消費型アイテムを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.UpdateItemMasterRequest.UpdateItemMasterRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.UpdateItemMasterResult.UpdateItemMasterResult
        """
        body = { 
            "max": request.get_max(),
        }
        if request.get_acquisition_item_trigger_script() is not None:
            body["acquisitionItemTriggerScript"] = request.get_acquisition_item_trigger_script()
        if request.get_acquisition_item_done_trigger_script() is not None:
            body["acquisitionItemDoneTriggerScript"] = request.get_acquisition_item_done_trigger_script()
        if request.get_consume_item_trigger_script() is not None:
            body["consumeItemTriggerScript"] = request.get_consume_item_trigger_script()
        if request.get_consume_item_done_trigger_script() is not None:
            body["consumeItemDoneTriggerScript"] = request.get_consume_item_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.UpdateItemMasterRequest import UpdateItemMasterRequest
        from gs2_consumable_item_client.control.UpdateItemMasterResult import UpdateItemMasterResult
        return UpdateItemMasterResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/master/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateItemMasterRequest.Constant.MODULE,
            target_function=UpdateItemMasterRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def create_item_pool(self, request):
        """
        消費型アイテムプールを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.CreateItemPoolRequest.CreateItemPoolRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.CreateItemPoolResult.CreateItemPoolResult
        """
        body = { 
            "name": request.get_name(),
            "serviceClass": request.get_service_class(),
        }

        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_acquisition_item_trigger_script() is not None:
            body["acquisitionItemTriggerScript"] = request.get_acquisition_item_trigger_script()
        if request.get_acquisition_item_done_trigger_script() is not None:
            body["acquisitionItemDoneTriggerScript"] = request.get_acquisition_item_done_trigger_script()
        if request.get_consume_item_trigger_script() is not None:
            body["consumeItemTriggerScript"] = request.get_consume_item_trigger_script()
        if request.get_consume_item_done_trigger_script() is not None:
            body["consumeItemDoneTriggerScript"] = request.get_consume_item_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.CreateItemPoolRequest import CreateItemPoolRequest
        from gs2_consumable_item_client.control.CreateItemPoolResult import CreateItemPoolResult
        return CreateItemPoolResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool",
            service=self.ENDPOINT,
            component=CreateItemPoolRequest.Constant.MODULE,
            target_function=CreateItemPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_item_pool(self, request):
        """
        消費型アイテムプールを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DeleteItemPoolRequest.DeleteItemPoolRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DeleteItemPoolRequest import DeleteItemPoolRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteItemPoolRequest.Constant.MODULE,
            target_function=DeleteItemPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_item_pool(self, request):
        """
        消費型アイテムプールの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DescribeItemPoolRequest.DescribeItemPoolRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.DescribeItemPoolResult.DescribeItemPoolResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DescribeItemPoolRequest import DescribeItemPoolRequest

        from gs2_consumable_item_client.control.DescribeItemPoolResult import DescribeItemPoolResult
        return DescribeItemPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool",
            service=self.ENDPOINT,
            component=DescribeItemPoolRequest.Constant.MODULE,
            target_function=DescribeItemPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_service_class(self, request):
        """
        サービスクラスの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DescribeServiceClassRequest.DescribeServiceClassRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.DescribeServiceClassResult.DescribeServiceClassResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DescribeServiceClassRequest import DescribeServiceClassRequest

        from gs2_consumable_item_client.control.DescribeServiceClassResult import DescribeServiceClassResult
        return DescribeServiceClassResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/serviceClass",
            service=self.ENDPOINT,
            component=DescribeServiceClassRequest.Constant.MODULE,
            target_function=DescribeServiceClassRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_item_pool(self, request):
        """
        消費型アイテムプールを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetItemPoolRequest.GetItemPoolRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetItemPoolResult.GetItemPoolResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetItemPoolRequest import GetItemPoolRequest

        from gs2_consumable_item_client.control.GetItemPoolResult import GetItemPoolResult
        return GetItemPoolResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "",
            service=self.ENDPOINT,
            component=GetItemPoolRequest.Constant.MODULE,
            target_function=GetItemPoolRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_item_pool_status(self, request):
        """
        消費型アイテムプールの状態を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetItemPoolStatusRequest.GetItemPoolStatusRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetItemPoolStatusResult.GetItemPoolStatusResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetItemPoolStatusRequest import GetItemPoolStatusRequest

        from gs2_consumable_item_client.control.GetItemPoolStatusResult import GetItemPoolStatusResult
        return GetItemPoolStatusResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/status",
            service=self.ENDPOINT,
            component=GetItemPoolStatusRequest.Constant.MODULE,
            target_function=GetItemPoolStatusRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_item_pool(self, request):
        """
        消費型アイテムプールを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.UpdateItemPoolRequest.UpdateItemPoolRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.UpdateItemPoolResult.UpdateItemPoolResult
        """
        body = { 
            "serviceClass": request.get_service_class(),
        }
        if request.get_description() is not None:
            body["description"] = request.get_description()
        if request.get_acquisition_item_trigger_script() is not None:
            body["acquisitionItemTriggerScript"] = request.get_acquisition_item_trigger_script()
        if request.get_acquisition_item_done_trigger_script() is not None:
            body["acquisitionItemDoneTriggerScript"] = request.get_acquisition_item_done_trigger_script()
        if request.get_consume_item_trigger_script() is not None:
            body["consumeItemTriggerScript"] = request.get_consume_item_trigger_script()
        if request.get_consume_item_done_trigger_script() is not None:
            body["consumeItemDoneTriggerScript"] = request.get_consume_item_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.UpdateItemPoolRequest import UpdateItemPoolRequest
        from gs2_consumable_item_client.control.UpdateItemPoolResult import UpdateItemPoolResult
        return UpdateItemPoolResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateItemPoolRequest.Constant.MODULE,
            target_function=UpdateItemPoolRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def export_master(self, request):
        """
        アイテムマスターデータをエクスポートする<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.ExportMasterRequest.ExportMasterRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.ExportMasterResult.ExportMasterResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.ExportMasterRequest import ExportMasterRequest

        from gs2_consumable_item_client.control.ExportMasterResult import ExportMasterResult
        return ExportMasterResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/master",
            service=self.ENDPOINT,
            component=ExportMasterRequest.Constant.MODULE,
            target_function=ExportMasterRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))
