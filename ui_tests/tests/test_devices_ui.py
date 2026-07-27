"""Playwright tests for device edit and delete workflows."""

from uuid import uuid4

import pytest
from playwright.sync_api import Page

from ui_tests.pages.devices_page import DevicesPage
from ui_tests.pages.login_page import LoginPage


pytestmark = [
    pytest.mark.ui,
    pytest.mark.auth,
    pytest.mark.regression,
]


def test_edit_device_through_ui(
    page: Page,
    base_url: str,
    test_username: str,
    test_password: str,
) -> None:
    """Verify that a device can be updated through the browser UI."""
    unique_suffix = uuid4().hex[:8]

    original_name = f"FCTEST-154-Edit-{unique_suffix}"
    updated_name = f"FCTEST-154-Updated-{unique_suffix}"

    login_page = LoginPage(
        page,
        base_url,
    )
    devices_page = DevicesPage(
        page,
        base_url,
    )

    login_page.open()
    login_page.login(
        test_username,
        test_password,
    )

    devices_page.assert_loaded()

    devices_page.create_device(
        name=original_name,
        status="online",
    )

    devices_page.assert_success_message(
        "Device created successfully."
    )
    devices_page.assert_device_visible(
        name=original_name,
        status="online",
    )

    devices_page.edit_device(
        current_name=original_name,
        updated_name=updated_name,
        updated_status="offline",
    )

    devices_page.assert_success_message(
        "Device updated successfully."
    )
    devices_page.assert_device_not_visible(
        original_name
    )
    devices_page.assert_device_visible(
        name=updated_name,
        status="offline",
    )


def test_delete_device_through_ui(
    page: Page,
    base_url: str,
    test_username: str,
    test_password: str,
) -> None:
    """Verify that a device can be deleted through the browser UI."""
    unique_suffix = uuid4().hex[:8]
    device_name = f"FCTEST-154-Delete-{unique_suffix}"

    login_page = LoginPage(
        page,
        base_url,
    )
    devices_page = DevicesPage(
        page,
        base_url,
    )

    login_page.open()
    login_page.login(
        test_username,
        test_password,
    )

    devices_page.assert_loaded()

    devices_page.create_device(
        name=device_name,
        status="online",
    )

    devices_page.assert_success_message(
        "Device created successfully."
    )
    devices_page.assert_device_visible(
        name=device_name,
        status="online",
    )

    devices_page.delete_device(device_name)

    devices_page.assert_success_message(
        "Device deleted successfully."
    )
    devices_page.assert_device_not_visible(
        device_name
    )