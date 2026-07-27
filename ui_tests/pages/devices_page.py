"""Page object for the Devices page."""

from playwright.sync_api import Locator, Page, expect

from ui_tests.pages.base_page import BasePage


class DevicesPage(BasePage):
    """Model the Devices page and its supported actions."""

    PATH = "/devices"

    def __init__(
        self,
        page: Page,
        base_url: str,
        timeout_ms: int = 10_000,
    ) -> None:
        super().__init__(
            page=page,
            base_url=base_url,
            timeout_ms=timeout_ms,
        )

        self.heading: Locator = page.get_by_role(
            "heading",
            name="Devices",
            exact=True,
        )

        self.create_name_input: Locator = page.get_by_test_id(
            "create-device-name"
        )
        self.create_status_select: Locator = page.get_by_test_id(
            "create-device-status"
        )
        self.create_submit_button: Locator = page.get_by_test_id(
            "create-device-submit"
        )

        self.edit_name_input: Locator = page.get_by_test_id(
            "edit-device-name"
        )
        self.edit_status_select: Locator = page.get_by_test_id(
            "edit-device-status"
        )
        self.edit_save_button: Locator = page.get_by_test_id(
            "edit-device-save"
        )
        self.edit_cancel_link: Locator = page.get_by_test_id(
            "edit-device-cancel"
        )

        self.success_message: Locator = page.get_by_test_id(
            "operation-success"
        )

    def assert_loaded(self) -> None:
        """Verify that the Devices page is displayed."""
        self.assert_url_contains(self.PATH)
        self.assert_visible(self.heading)

    def open(self) -> None:
        """Open the Devices page."""
        self.navigate(self.PATH)

    def is_loaded(self) -> bool:
        """Return whether the browser is currently on the Devices page."""
        return self.PATH in self.page.url

    @property
    def device_rows(self) -> Locator:
        """Return all device table rows."""
        return self.page.locator(
            '[data-testid^="device-row-"]'
        )

    @property
    def device_items(self) -> Locator:
        """Return the current device rows.

        This property is retained for compatibility with existing tests.
        """
        return self.device_rows

    def device_count(self) -> int:
        """Return the number of displayed devices."""
        return self.device_rows.count()

    def assert_has_devices(self) -> None:
        """Assert that at least one device is displayed."""
        count = self.device_count()

        assert count > 0, (
            "Expected at least one device to be displayed, "
            "but the device list was empty"
        )

        self.assert_visible(self.device_rows.first)

    def device_row(self, device_name: str) -> Locator:
        """Return the device row containing an exact device name."""
        return self.device_rows.filter(
            has=self.page.get_by_text(
                device_name,
                exact=True,
            )
        )

    def edit_button(self, device_name: str) -> Locator:
        """Return the Edit button for a device."""
        return self.device_row(device_name).get_by_role(
            "button",
            name=f"Edit {device_name}",
            exact=True,
        )

    def delete_button(self, device_name: str) -> Locator:
        """Return the Delete button for a device."""
        return self.device_row(device_name).get_by_role(
            "button",
            name=f"Delete {device_name}",
            exact=True,
        )

    def create_device(
        self,
        name: str,
        status: str,
    ) -> None:
        """Create a device through the browser UI."""
        self.fill(self.create_name_input, name)

        expect(
            self.create_status_select
        ).to_be_visible(timeout=self.timeout_ms)

        self.create_status_select.select_option(status)

        self.click(self.create_submit_button)

        self.assert_loaded()

    def open_edit_form(self, device_name: str) -> None:
        """Open the edit form for a named device."""
        self.click(self.edit_button(device_name))

        self.assert_url_contains("/edit")
        self.assert_visible(self.edit_name_input)
        self.assert_visible(self.edit_status_select)
        self.assert_visible(self.edit_save_button)

    def edit_device(
        self,
        current_name: str,
        updated_name: str,
        updated_status: str,
    ) -> None:
        """Update a device through the browser UI."""
        self.open_edit_form(current_name)

        self.fill(
            self.edit_name_input,
            updated_name,
        )

        self.edit_status_select.select_option(
            updated_status
        )

        self.click(self.edit_save_button)

        self.assert_loaded()

    def delete_device(self, device_name: str) -> None:
        """Delete a device and accept the confirmation dialog."""
        delete_button = self.delete_button(device_name)

        expect(
            delete_button
        ).to_be_visible(timeout=self.timeout_ms)

        dialog_details: dict[str, str] = {}

        def handle_dialog(dialog) -> None:
            dialog_details["type"] = dialog.type
            dialog_details["message"] = dialog.message
            dialog.accept()

        self.page.once(
            "dialog",
            handle_dialog,
        )

        delete_button.click()

        assert dialog_details.get("type") == "confirm", (
            "Expected a confirmation dialog, "
            f"but received {dialog_details.get('type')!r}"
        )

        assert device_name in dialog_details.get("message", ""), (
            f"Expected confirmation message to contain {device_name!r}, "
            f"but it was {dialog_details.get('message')!r}"
        )

        self.assert_loaded()

    def assert_device_visible(
        self,
        name: str,
        status: str | None = None,
    ) -> None:
        """Assert that a device is present in the table."""
        row = self.device_row(name)

        expect(row).to_have_count(
            1,
            timeout=self.timeout_ms,
        )
        expect(row).to_be_visible(
            timeout=self.timeout_ms,
        )

        expect(
            row.get_by_text(
                name,
                exact=True,
            )
        ).to_be_visible(timeout=self.timeout_ms)

        if status is not None:
            expect(
                row.get_by_text(
                    status,
                    exact=True,
                )
            ).to_be_visible(timeout=self.timeout_ms)

    def assert_device_not_visible(
        self,
        device_name: str,
    ) -> None:
        """Assert that a device is absent from the table."""
        expect(
            self.device_row(device_name)
        ).to_have_count(
            0,
            timeout=self.timeout_ms,
        )

    def assert_success_message(
        self,
        expected_message: str,
    ) -> None:
        """Assert that the expected operation message is displayed."""
        self.assert_exact_text(
            self.success_message,
            expected_message,
        )