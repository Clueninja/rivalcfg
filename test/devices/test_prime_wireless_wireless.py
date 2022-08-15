import pytest

from rivalcfg import usbhid
from rivalcfg import mouse
from rivalcfg.devices import prime_wireless_wireless
from rivalcfg import mouse_settings


class TestDevice(object):
    @pytest.fixture
    def mouse(self):
        settings = mouse_settings.FakeMouseSettings(
            0x1038,
            0xBAAD,
            prime_wireless_wireless.profile,
        )
        return mouse.Mouse(
            usbhid.FakeDevice(),
            prime_wireless_wireless.profile,
            settings,
        )

    @pytest.mark.parametrize(
        "value,expected_hid_report",
        [
            (100, b"\x02\x00\x6d\x01\x00\x00"),
            (200, b"\x02\x00\x6d\x01\x00\x01"),
            (300, b"\x02\x00\x6d\x01\x00\x02"),
            (18000, b"\x02\x00\x6d\x01\x00\xD6"),
            ("200,400", b"\x02\x00\x6d\x02\x00\x01\x03"),
            ("200,400,800,1600", b"\x02\x00\x6d\x04\x00\x01\x03\x08\x11"),
        ],
    )
    def test_set_sensitivity(self, mouse, value, expected_hid_report):
        mouse.set_sensitivity(value)
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == expected_hid_report

    @pytest.mark.parametrize(
        "value,expected_hid_report",
        [
            (125, b"\x02\x00\x6B\x03"),
            (250, b"\x02\x00\x6B\x02"),
            (500, b"\x02\x00\x6B\x01"),
            (1000, b"\x02\x00\x6B\x00"),
        ],
    )
    def test_set_polling_rate(self, mouse, value, expected_hid_report):
        mouse.set_polling_rate(value)
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == expected_hid_report

    @pytest.mark.parametrize(
        "value,expected_hid_report",
        [
            ("#ABCDEF", b"\x02\x00\x61\x01\x00\xAB\xCD\xEF"),
            ("red", b"\x02\x00\x61\x01\x00\xFF\x00\x00"),
        ],
    )
    def test_set_color(self, mouse, value, expected_hid_report):
        mouse.set_color(value)
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == expected_hid_report

    @pytest.mark.parametrize(
        "value,expected_hid_report",
        [
            (
                "default",
                b"\x02\x00\x6A\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x03\x00\x00\x00\x00\x04\x00\x00\x00\x00\x05\x00\x00\x00\x00\x30\x00\x00\x00\x00\x31\x00\x00\x00\x00\x32\x00\x00\x00\x00",
            ),
            (
                "buttons(button2=button6)",
                b"\x02\x00\x6A\x01\x00\x00\x00\x00\x06\x00\x00\x00\x00\x03\x00\x00\x00\x00\x04\x00\x00\x00\x00\x05\x00\x00\x00\x00\x30\x00\x00\x00\x00\x31\x00\x00\x00\x00\x32\x00\x00\x00\x00",
            ),
            (
                {"buttons": {"button2": "button6"}},
                b"\x02\x00\x6A\x01\x00\x00\x00\x00\x06\x00\x00\x00\x00\x03\x00\x00\x00\x00\x04\x00\x00\x00\x00\x05\x00\x00\x00\x00\x30\x00\x00\x00\x00\x31\x00\x00\x00\x00\x32\x00\x00\x00\x00",
            ),
            (
                "buttons(ScrollUp=ScrollDown; ScrollDown=ScrollUp)",
                b"\x02\x00\x6A\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x03\x00\x00\x00\x00\x04\x00\x00\x00\x00\x05\x00\x00\x00\x00\x30\x00\x00\x00\x00\x32\x00\x00\x00\x00\x31\x00\x00\x00\x00",
            ),
        ],
    )
    def test_set_buttons_mapping(self, mouse, value, expected_hid_report):
        mouse.set_buttons_mapping(value)
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == expected_hid_report

    def test_battery_level(self, mouse):
        battery_info = mouse.battery
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == b"\x02\x00\xd2"
        assert "is_charging" in battery_info
        assert "level" in battery_info

    def test_save(self, mouse):
        mouse.save()
        mouse._hid_device.bytes.seek(0)
        hid_report = mouse._hid_device.bytes.read()
        assert hid_report == b"\x02\x00\x51\x00"
