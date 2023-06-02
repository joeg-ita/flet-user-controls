import flet as ft
import pytz

from analog_clock import AnalogClock

def main(page: ft.Page):

    rows = ft.Column([
        ft.Row(
        [
            ft.Container(AnalogClock(clock_label="London",timezone="GMT"), width=200, height=200,),
            ft.Container(AnalogClock(), width=200, height=200),
            ft.Container(AnalogClock(clock_label = "Moscow", timezone="Europe/Moscow"), width=200, height=200),
        ], spacing=50),
        ft.Row(
        [
            ft.Container(AnalogClock(clock_label = "New York", timezone="America/New_York"), width=200, height=200),
            ft.Container(AnalogClock(clock_label="Los Angeles",timezone="America/Los_Angeles"), width=200, height=200),
            ft.Container(AnalogClock(clock_label="Honolulu",timezone="Pacific/Honolulu"), width=200, height=200,),
        ], spacing=50)
    ], spacing=50
    
    )


    page.add(rows)

ft.app(main)