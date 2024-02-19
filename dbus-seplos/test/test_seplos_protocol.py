# -*- coding: utf-8 -*-

from seplos_protocol import int_from_ascii, is_valid_hex_string, is_valid_length
from seplos_protocol import get_checksum, get_info_length, encode_cmd


def test_int_from_ascii_1():
    data = b'0x00'
    offset = 0
    signed = False
    size = 2
    result = int_from_ascii(data, offset, signed, size)
    assert result == 0


def test_int_from_ascii_2():
    data = b'1000'
    offset = 0
    signed = False
    size = 2
    result = int_from_ascii(data, offset, signed, size)
    assert result == 4096


def test_int_from_ascii_3():
    data = b'0010'
    offset = 0
    signed = False
    size = 2
    result = int_from_ascii(data, offset, signed, size)
    assert result == 16


def test_int_from_ascii_4():
    data = b'00100000'
    offset = 1
    signed = False
    size = 2
    result = int_from_ascii(data, offset, signed, size)
    assert result == 4096


def test_int_from_ascii_5():
    data = b'00100000'
    offset = 0
    signed = False
    size = 4
    result = int_from_ascii(data, offset, signed, size)
    assert result == 1048576


def test_is_valid_hex_string_1():
    data = b'1203400456ABCEFE'
    result = is_valid_hex_string(data)
    assert result


def test_is_valid_hex_string_2():
    data = b'1203xf.,456ABCEFE'
    result = is_valid_hex_string(data)
    assert not result


def test_is_valid_length_1():
    data = b'1203400456ABCEFE'
    expected_length = 16
    result = is_valid_length(data, expected_length)
    assert result


def test_is_valid_length_2():
    data = b'1203400456ABCEFE'
    expected_length = 15
    result = is_valid_length(data, expected_length)
    assert not result


def test_get_checksum_1():
    frame = b'1203400456ABCEFE'
    result = get_checksum(frame)
    assert result == 64625


def test_get_info_length_1():
    info = b'1203400456ABCEFE'
    result = get_info_length(info)
    assert result == 61456


def test_encode_cmd_1():
    address = 0x00
    cid2 = 0x42
    info = b'-00200'
    result = encode_cmd(address, cid2, info)
    assert result == b'~20004642A006-00200FC78\r'
