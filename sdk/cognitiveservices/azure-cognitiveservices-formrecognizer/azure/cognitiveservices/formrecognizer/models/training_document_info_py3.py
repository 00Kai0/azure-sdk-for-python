# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TrainingDocumentInfo(Model):
    """Report for a custom model training document.

    All required parameters must be populated in order to send to Azure.

    :param document_name: Required. Training document name.
    :type document_name: str
    :param pages: Required. Total number of pages trained.
    :type pages: int
    :param errors: Required. List of errors.
    :type errors: list[str]
    :param status: Required. Status of the training operation. Possible values
     include: 'succeeded', 'partiallySucceeded', 'failed'
    :type status: str or
     ~azure.cognitiveservices.formrecognizer.models.TrainStatus
    """

    _validation = {
        'document_name': {'required': True},
        'pages': {'required': True},
        'errors': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'document_name': {'key': 'documentName', 'type': 'str'},
        'pages': {'key': 'pages', 'type': 'int'},
        'errors': {'key': 'errors', 'type': '[str]'},
        'status': {'key': 'status', 'type': 'TrainStatus'},
    }

    def __init__(self, *, document_name: str, pages: int, errors, status, **kwargs) -> None:
        super(TrainingDocumentInfo, self).__init__(**kwargs)
        self.document_name = document_name
        self.pages = pages
        self.errors = errors
        self.status = status
