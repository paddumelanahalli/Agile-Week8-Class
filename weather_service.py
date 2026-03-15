#test_alerts.py

from unittest.mock import patch
from weather_service import check_hurricane_safety


# We "patch" the function that actually talks to the internet
@patch('weather_service.get_wind_speed')
def test_hurricane_alert_trigger(mock_wind):
    # We FORCE the fake API to return 120 mph
    mock_wind.return_value = 120

    # Even if the real weather is sunny, our test "sees" a hurricane
    assert check_hurricane_safety() == "EVACUATE"

#weather_service.py
def get_wind_speed():
    # In reality, this would use 'requests' to call a URL
    # For now, it's just a placeholder
    pass
"""
def check_hurricane_safety():
    speed = get_wind_speed()
    if speed > 100:
        return "EVACUATE"
    return "SAFE"
"""
def check_hurricane_safety():
    try:
        speed = get_wind_speed()
        if speed is None:
            return "SYSTEM ERROR"
        return "EVACUATE" if speed > 100 else "SAFE"
    except Exception:
        return "SERVICE DOWN"
