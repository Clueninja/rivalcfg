from .. import usbhid


profile = {
    "name": "SteelSeries Rival 650 Wireless",
    "models": [
        {
            "name": "SteelSeries Rival 650 Wireless (wired mode)",
            "vendor_id": 0x1038,
            "product_id": 0x172B,
            "endpoint": 0,
        },
        {
            "name": "SteelSeries Rival 650 Wireless (2.4 GHz wireless mode)",
            "vendor_id": 0x1038,
            "product_id": 0x1726,
            "endpoint": 0,
        },
    ],
    "settings": {
        "sensitivity1": {
            "label": "Sensitivity preset 1",
            "description": "Set sensitivity preset 1 (DPI)",
            "cli": ["-s", "--sensitivity1"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x15, 0x01],
            "value_type": "range",
            "input_range": [100, 12000, 100],
            "output_range": [0x00, 0x77, 1],
            "default": 800,
        },
        "sensitivity2": {
            "label": "Sensitivity preset 2",
            "description": "Set sensitivity preset 2 (DPI)",
            "cli": ["-S", "--sensitivity2"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x15, 0x02],
            "value_type": "range",
            "input_range": [100, 12000, 100],
            "output_range": [0x00, 0x77, 1],
            "default": 1600,
        },
        "polling_rate": {
            "label": "Polling rate",
            "description": "Set the polling rate (Hz)",
            "cli": ["-p", "--polling-rate"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x17],
            "value_type": "choice",
            "choices": {
                125: 0x04,
                250: 0x03,
                500: 0x02,
                1000: 0x01,
            },
            "default": 1000,
        },
        "buttons_mapping": {
            "label": "Buttons mapping",
            "description": "Set the mapping of the buttons",
            "cli": ["-b", "--buttons"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x19],
            "value_type": "buttons",
            # fmt: off
            "buttons": {
                "Button1": {"id": 0x01, "offset": 0x00, "default": "button1"},
                "Button2": {"id": 0x02, "offset": 0x05, "default": "button2"},
                "Button3": {"id": 0x03, "offset": 0x0A, "default": "button3"},
                "Button4": {"id": 0x04, "offset": 0x0F, "default": "button4"},
                "Button5": {"id": 0x05, "offset": 0x14, "default": "button5"},
                "Button6": {"id": 0x06, "offset": 0x19, "default": "disabled"},
                "Button7": {"id": 0x00, "offset": 0x1E, "default": "dpi"},
            },
            "button_field_length": 5,
            "button_disable":     0x00,
            "button_keyboard":    0x51,
            "button_multimedia":  0x61,
            "button_dpi_switch":  0x30,
            "button_scroll_up":   0x31,
            "button_scroll_down": 0x32,
            # fmt: on
            "default": "buttons(button1=button1; button2=button2; button3=button3; button4=button4; button5=button5; button6=disabled; button7=dpi)",
        },
        "sleep_timer": {
            "label": "Sleep timer",
            "description": "Set the IDLE time before the mouse goes to sleep mode (minutes)",
            "cli": ["-t", "--sleep-timer"],
            "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
            "command": [0x2B, 0x01, 0x01, 0x00, 0x00, 0x00],
            "value_type": "range",
            "input_range": [1, 20, 1],
            "output_range": [0x003C, 0x04B0, 60],
            "range_length_byte": 2,
            "default": 5,
        },
    },
    "battery_level": {
        "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
        "command": [0xAA, 0x01],
        "response_length": 3,
        "is_charging": lambda data: bool(data[2]),
        "level": lambda data: int(data[0]),
    },
    "save_command": {
        "report_type": usbhid.HID_REPORT_TYPE_OUTPUT,
        "command": [0x09],
    },
}
