from dataclasses import dataclass


@dataclass
class Flight:
    departure_time: str
    arrival_time: str
    departure_airport: str
    arrival_airport: str
    flight: str


flight = Flight(
    departure_time='06:10',
    arrival_time='07:45',
    departure_airport='BKK Suvarnabhumi Airport, Bangkok',
    arrival_airport='USM Koh Samui Airport',
    flight='1h 35m flight #PG109 with Bangkok Air in Economy'
)
