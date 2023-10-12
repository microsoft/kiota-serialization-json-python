import json
from datetime import date, datetime, time, timedelta
from uuid import UUID

import pytest

from kiota_serialization_json.json_parse_node import JsonParseNode

from ..helpers import OfficeLocation, User

url: str = "https://graph.microsoft.com/v1.0/$metadata#users/$entity"


def test_get_str_value():
    parse_node = JsonParseNode("Diego Siciliani")
    result = parse_node.get_str_value()
    assert result == "Diego Siciliani"


def test_get_int_value():
    parse_node = JsonParseNode(1454)
    result = parse_node.get_int_value()
    assert result == 1454


def test_get_bool_value():
    parse_node = JsonParseNode(False)
    result = parse_node.get_bool_value()
    assert result is False


def test_get_float_value():
    parse_node = JsonParseNode(44.6)
    result = parse_node.get_float_value()
    assert result == 44.6


def test_get_uuid_value():
    parse_node = JsonParseNode("f58411c7-ae78-4d3c-bb0d-3f24d948de41")
    result = parse_node.get_uuid_value()
    assert result == UUID("f58411c7-ae78-4d3c-bb0d-3f24d948de41")


def test_get_datetime_value():
    parse_node = JsonParseNode('2022-01-27T12:59:45.596117')
    result = parse_node.get_datetime_value()
    assert isinstance(result, datetime)


def test_get_date_value():
    parse_node = JsonParseNode('2015-04-20')
    result = parse_node.get_date_value()
    assert isinstance(result, date)
    assert str(result) == '2015-04-20'


def test_get_time_value():
    parse_node = JsonParseNode('12:59:45.596117')
    result = parse_node.get_time_value()
    assert isinstance(result, time)
    assert str(result) == '12:59:45.596117'


def test_get_timedelta_value():
    parse_node = JsonParseNode('PT30S')
    result = parse_node.get_timedelta_value()
    assert isinstance(result, timedelta)
    assert str(result) == '0:00:30'


def test_get_collection_of_primitive_values():
    parse_node = JsonParseNode([12.1, 12.2, 12.3, 12.4, 12.5])
    result = parse_node.get_collection_of_primitive_values(float)
    assert result == [12.1, 12.2, 12.3, 12.4, 12.5]


def test_get_collection_of_primitive_values_no_type():
    parse_node = JsonParseNode(["One", "Two", "Three", "Four", "Five"])
    result = parse_node.get_collection_of_primitive_values(None)
    assert result == ["One", "Two", "Three", "Four", "Five"]


def test_get_bytes_value():
    parse_node = JsonParseNode('U2Ftd2VsIGlzIHRoZSBiZXN0')
    result = parse_node.get_bytes_value()
    assert isinstance(result, bytes)


def test_get_collection_of_enum_values():
    parse_node = JsonParseNode(["dunhill", "oval"])
    result = parse_node.get_collection_of_enum_values(OfficeLocation)
    assert isinstance(result, list)
    assert result == [OfficeLocation.Dunhill, OfficeLocation.Oval]


def test_get_enum_value():
    parse_node = JsonParseNode("dunhill")
    result = parse_node.get_enum_value(OfficeLocation)
    assert isinstance(result, OfficeLocation)
    assert result == OfficeLocation.Dunhill


def test_get_object_value(user1_json):
    parse_node = JsonParseNode(json.loads(user1_json))
    result = parse_node.get_object_value(User)
    assert isinstance(result, User)
    assert result.id == UUID("8f841f30-e6e3-439a-a812-ebd369559c36")
    assert result.office_location == OfficeLocation.Dunhill
    assert isinstance(result.updated_at, datetime)
    assert isinstance(result.birthday, date)
    assert result.business_phones == ["+1 205 555 0108"]
    assert result.is_active is True
    assert result.mobile_phone is None


def test_get_collection_of_object_values(users_json):
    parse_node = JsonParseNode(json.loads(users_json))
    result = parse_node.get_collection_of_object_values(User)
    assert isinstance(result[0], User)
    assert result[0].id == UUID("8f841f30-e6e3-439a-a812-ebd369559c36")
    assert result[0].office_location == OfficeLocation.Dunhill
    assert isinstance(result[0].updated_at, datetime)
    assert isinstance(result[0].birthday, date)
    assert result[0].business_phones == ["+1 205 555 0108"]
    assert result[0].is_active is True
    assert result[0].mobile_phone is None
