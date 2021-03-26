import os
import tempfile
from pathlib import Path

import pytest
from packaging_tools.auto_codegen import update_servicemetadata


"""
Create metadata file

Update metadata file

Update MANIFETS.IN

No need to update MANIFETS.IN

Exception thrown from update_service_metadata

"""

class TestServiceMetadata:

    def setUp(self):
        self.sdk_folder = "sdk"
        self.data = {
            "specFolder": "../azure-rest-api-specs",
            "headSha": "e295fe97eee3709668d3e5f7f8b434026b814ef9",
            "headRef": "master",
            "repoHttpsUrl": "https://github.com/Azure/azure-rest-api-specs",
        }
        self.config = {
            "meta": {
                "autorest_options": {
                    "version": "3.0.6369",
                    "use": "@autorest/python@5.4.3",
                    "python": "",
                    "python-mode": "update",
                    "sdkrel:python-sdks-folder": "./sdk/.",
                    "multiapi": "",
                    "track2": ""
                },
                "advanced_options": {
                    "create_sdk_pull_requests": true,
                    "sdk_generation_pull_request_base": "integration_branch"
                },
                "repotag": "azure-sdk-for-python-track2",
                "version": "0.2.0"
            },
            "projects": {
                "./azure-rest-api-specs/specification/operationalinsights/resource-manager/readme.md": {}
            }

        }
        self.folder_name = "monitor"
        self.package_name = "azure-mgmt-monitor"
        self.spec_folder = "./"
        self.input_readme = "azure-rest-api-specs/specification/operationalinsights/resource-manager/readme.md"

    def test_create_metadata(self):

        with tempfile.TemporaryDirectory() as temp_dir:
            self.sdk_folder = str(Path(temp_dir, "sdk"))
            self.spec_folder = str(Path(temp_dir, "spec"))
            os.mkdirs(self.sdk_folder)
            os.mkdirs(self.spec_folder)

            update_servicemetadata(
                sdk_folder=self.sdk_folder,
                data=self.data,
                config=self.config,
                folder_name=self.folder_name,
                package_name=self.package_name,
                spec_folder=self.spec_folder,
                input_readme=self.input_readme
            )

    def test_update_metadata(self):
        pass

    def test_update_manifest(self):
        pass

    def test_no_need_to_update_manifest(self):
        pass
