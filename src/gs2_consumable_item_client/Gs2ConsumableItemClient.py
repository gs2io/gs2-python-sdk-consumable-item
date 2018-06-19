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

    def acquisition_inventory(self, request):
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
        :type request: gs2_consumable_item_client.control.AcquisitionInventoryRequest.AcquisitionInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.AcquisitionInventoryResult.AcquisitionInventoryResult
        """
        body = { 
            "count": request.get_count(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.AcquisitionInventoryRequest import AcquisitionInventoryRequest
        from gs2_consumable_item_client.control.AcquisitionInventoryResult import AcquisitionInventoryResult
        return AcquisitionInventoryResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "",
            service=self.ENDPOINT,
            component=AcquisitionInventoryRequest.Constant.MODULE,
            target_function=AcquisitionInventoryRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def acquisition_inventory_by_stamp_sheet(self, request):
        """
        スタンプシートを使用してインベントリにアイテムを加えます<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.AcquisitionInventoryByStampSheetRequest.AcquisitionInventoryByStampSheetRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.AcquisitionInventoryByStampSheetResult.AcquisitionInventoryByStampSheetResult
        """
        body = { 
            "sheet": request.get_sheet(),
            "keyName": request.get_key_name(),
        }

        if request.get_max_value() is not None:
            body["maxValue"] = request.get_max_value()
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.AcquisitionInventoryByStampSheetRequest import AcquisitionInventoryByStampSheetRequest
        from gs2_consumable_item_client.control.AcquisitionInventoryByStampSheetResult import AcquisitionInventoryByStampSheetResult
        return AcquisitionInventoryByStampSheetResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/item",
            service=self.ENDPOINT,
            component=AcquisitionInventoryByStampSheetRequest.Constant.MODULE,
            target_function=AcquisitionInventoryByStampSheetRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def acquisition_my_inventory(self, request):
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
        :type request: gs2_consumable_item_client.control.AcquisitionMyInventoryRequest.AcquisitionMyInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.AcquisitionMyInventoryResult.AcquisitionMyInventoryResult
        """
        body = { 
            "count": request.get_count(),
        }

        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.AcquisitionMyInventoryRequest import AcquisitionMyInventoryRequest
        from gs2_consumable_item_client.control.AcquisitionMyInventoryResult import AcquisitionMyInventoryResult
        return AcquisitionMyInventoryResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "/my",
            service=self.ENDPOINT,
            component=AcquisitionMyInventoryRequest.Constant.MODULE,
            target_function=AcquisitionMyInventoryRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def consume_inventory(self, request):
        """
        インベントリのアイテムを消費します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.ConsumeInventoryRequest.ConsumeInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.ConsumeInventoryResult.ConsumeInventoryResult
        """
        body = { 
            "count": request.get_count(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.ConsumeInventoryRequest import ConsumeInventoryRequest
        from gs2_consumable_item_client.control.ConsumeInventoryResult import ConsumeInventoryResult
        return ConsumeInventoryResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "",
            service=self.ENDPOINT,
            component=ConsumeInventoryRequest.Constant.MODULE,
            target_function=ConsumeInventoryRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def consume_inventory_by_stamp_task(self, request):
        """
        スタンプタスクを使用してインベントリのアイテムを消費します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.ConsumeInventoryByStampTaskRequest.ConsumeInventoryByStampTaskRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.ConsumeInventoryByStampTaskResult.ConsumeInventoryByStampTaskResult
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
        from gs2_consumable_item_client.control.ConsumeInventoryByStampTaskRequest import ConsumeInventoryByStampTaskRequest
        from gs2_consumable_item_client.control.ConsumeInventoryByStampTaskResult import ConsumeInventoryByStampTaskResult
        return ConsumeInventoryByStampTaskResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/item",
            service=self.ENDPOINT,
            component=ConsumeInventoryByStampTaskRequest.Constant.MODULE,
            target_function=ConsumeInventoryByStampTaskRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def consume_my_inventory(self, request):
        """
        インベントリのアイテムを消費します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.ConsumeMyInventoryRequest.ConsumeMyInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.ConsumeMyInventoryResult.ConsumeMyInventoryResult
        """
        body = { 
            "count": request.get_count(),
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.ConsumeMyInventoryRequest import ConsumeMyInventoryRequest
        from gs2_consumable_item_client.control.ConsumeMyInventoryResult import ConsumeMyInventoryResult
        return ConsumeMyInventoryResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "/my",
            service=self.ENDPOINT,
            component=ConsumeMyInventoryRequest.Constant.MODULE,
            target_function=ConsumeMyInventoryRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_inventory(self, request):
        """
        インベントリからアイテムを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DeleteInventoryRequest.DeleteInventoryRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DeleteInventoryRequest import DeleteInventoryRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "",
            service=self.ENDPOINT,
            component=DeleteInventoryRequest.Constant.MODULE,
            target_function=DeleteInventoryRequest.Constant.FUNCTION,
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
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DescribeInventoryRequest import DescribeInventoryRequest

        from gs2_consumable_item_client.control.DescribeInventoryResult import DescribeInventoryResult
        return DescribeInventoryResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "",
            service=self.ENDPOINT,
            component=DescribeInventoryRequest.Constant.MODULE,
            target_function=DescribeInventoryRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def describe_my_inventory(self, request):
        """
        ユーザが所持しているインベントリの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DescribeMyInventoryRequest.DescribeMyInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.DescribeMyInventoryResult.DescribeMyInventoryResult
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
        from gs2_consumable_item_client.control.DescribeMyInventoryRequest import DescribeMyInventoryRequest

        from gs2_consumable_item_client.control.DescribeMyInventoryResult import DescribeMyInventoryResult
        return DescribeMyInventoryResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/my",
            service=self.ENDPOINT,
            component=DescribeMyInventoryRequest.Constant.MODULE,
            target_function=DescribeMyInventoryRequest.Constant.FUNCTION,
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
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetInventoryRequest import GetInventoryRequest

        from gs2_consumable_item_client.control.GetInventoryResult import GetInventoryResult
        return GetInventoryResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "/user/" + str(("null" if request.get_user_id() is None or request.get_user_id() == "" else url_encoder.encode(request.get_user_id()))) + "",
            service=self.ENDPOINT,
            component=GetInventoryRequest.Constant.MODULE,
            target_function=GetInventoryRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_my_inventory(self, request):
        """
        インベントリの内容を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetMyInventoryRequest.GetMyInventoryRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetMyInventoryResult.GetMyInventoryResult
        """
        query_strings = {
        }
        headers = { 
            "X-GS2-ACCESS-TOKEN": request.get_access_token()
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetMyInventoryRequest import GetMyInventoryRequest

        from gs2_consumable_item_client.control.GetMyInventoryResult import GetMyInventoryResult
        return GetMyInventoryResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "/my",
            service=self.ENDPOINT,
            component=GetMyInventoryRequest.Constant.MODULE,
            target_function=GetMyInventoryRequest.Constant.FUNCTION,
            query_strings=query_strings,
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
        if request.get_acquisition_inventory_trigger_script() is not None:
            body["acquisitionInventoryTriggerScript"] = request.get_acquisition_inventory_trigger_script()
        if request.get_acquisition_inventory_done_trigger_script() is not None:
            body["acquisitionInventoryDoneTriggerScript"] = request.get_acquisition_inventory_done_trigger_script()
        if request.get_consume_inventory_trigger_script() is not None:
            body["consumeInventoryTriggerScript"] = request.get_consume_inventory_trigger_script()
        if request.get_consume_inventory_done_trigger_script() is not None:
            body["consumeInventoryDoneTriggerScript"] = request.get_consume_inventory_done_trigger_script()
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
        if request.get_acquisition_inventory_trigger_script() is not None:
            body["acquisitionInventoryTriggerScript"] = request.get_acquisition_inventory_trigger_script()
        if request.get_acquisition_inventory_done_trigger_script() is not None:
            body["acquisitionInventoryDoneTriggerScript"] = request.get_acquisition_inventory_done_trigger_script()
        if request.get_consume_inventory_trigger_script() is not None:
            body["consumeInventoryTriggerScript"] = request.get_consume_inventory_trigger_script()
        if request.get_consume_inventory_done_trigger_script() is not None:
            body["consumeInventoryDoneTriggerScript"] = request.get_consume_inventory_done_trigger_script()
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

    def create_item(self, request):
        """
        消費型アイテムを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.CreateItemRequest.CreateItemRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.CreateItemResult.CreateItemResult
        """
        body = { 
            "name": request.get_name(),
            "max": request.get_max(),
        }

        if request.get_acquisition_inventory_trigger_script() is not None:
            body["acquisitionInventoryTriggerScript"] = request.get_acquisition_inventory_trigger_script()
        if request.get_acquisition_inventory_done_trigger_script() is not None:
            body["acquisitionInventoryDoneTriggerScript"] = request.get_acquisition_inventory_done_trigger_script()
        if request.get_consume_inventory_trigger_script() is not None:
            body["consumeInventoryTriggerScript"] = request.get_consume_inventory_trigger_script()
        if request.get_consume_inventory_done_trigger_script() is not None:
            body["consumeInventoryDoneTriggerScript"] = request.get_consume_inventory_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.CreateItemRequest import CreateItemRequest
        from gs2_consumable_item_client.control.CreateItemResult import CreateItemResult
        return CreateItemResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item",
            service=self.ENDPOINT,
            component=CreateItemRequest.Constant.MODULE,
            target_function=CreateItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))

    def delete_item(self, request):
        """
        消費型アイテムを削除します<br>
        <br>
        既にアイテムを所持しているユーザがいる場合、そのアイテムはインベントリから削除されることはありません。<br>
        消費型アイテムを削除することで新しくアイテムを付与することはできなくなりますが、消費することは出来ます。<br>
        <br>
        これを防ぎたい場合はすべてのユーザのインベントリを走査して該当アイテムを削除する必要があります。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DeleteItemRequest.DeleteItemRequest
        """
        query_strings = {}
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DeleteItemRequest import DeleteItemRequest
        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=DeleteItemRequest.Constant.MODULE,
            target_function=DeleteItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )

    def describe_item(self, request):
        """
        消費型アイテムの一覧を取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.DescribeItemRequest.DescribeItemRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.DescribeItemResult.DescribeItemResult
        """
        query_strings = {
            'pageToken': request.get_page_token(),
            'limit': request.get_limit(),
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.DescribeItemRequest import DescribeItemRequest

        from gs2_consumable_item_client.control.DescribeItemResult import DescribeItemResult
        return DescribeItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item",
            service=self.ENDPOINT,
            component=DescribeItemRequest.Constant.MODULE,
            target_function=DescribeItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def get_item(self, request):
        """
        消費型アイテムを取得します<br>
        <br>:param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.GetItemRequest.GetItemRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.GetItemResult.GetItemResult
        """
        query_strings = {
        }
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.GetItemRequest import GetItemRequest

        from gs2_consumable_item_client.control.GetItemResult import GetItemResult
        return GetItemResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=GetItemRequest.Constant.MODULE,
            target_function=GetItemRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))

    def update_item(self, request):
        """
        消費型アイテムを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_consumable_item_client.control.UpdateItemRequest.UpdateItemRequest
        :return: 結果
        :rtype: gs2_consumable_item_client.control.UpdateItemResult.UpdateItemResult
        """
        body = { 
            "max": request.get_max(),
        }
        if request.get_acquisition_inventory_trigger_script() is not None:
            body["acquisitionInventoryTriggerScript"] = request.get_acquisition_inventory_trigger_script()
        if request.get_acquisition_inventory_done_trigger_script() is not None:
            body["acquisitionInventoryDoneTriggerScript"] = request.get_acquisition_inventory_done_trigger_script()
        if request.get_consume_inventory_trigger_script() is not None:
            body["consumeInventoryTriggerScript"] = request.get_consume_inventory_trigger_script()
        if request.get_consume_inventory_done_trigger_script() is not None:
            body["consumeInventoryDoneTriggerScript"] = request.get_consume_inventory_done_trigger_script()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_consumable_item_client.control.UpdateItemRequest import UpdateItemRequest
        from gs2_consumable_item_client.control.UpdateItemResult import UpdateItemResult
        return UpdateItemResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/itemPool/" + str(("null" if request.get_item_pool_name() is None or request.get_item_pool_name() == "" else url_encoder.encode(request.get_item_pool_name()))) + "/item/" + str(("null" if request.get_item_name() is None or request.get_item_name() == "" else url_encoder.encode(request.get_item_name()))) + "",
            service=self.ENDPOINT,
            component=UpdateItemRequest.Constant.MODULE,
            target_function=UpdateItemRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))
