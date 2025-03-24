import json

from src.file_handler import JsonFileHandler


def test_init_creates_file(mock_exists, mock_open):
    handler = JsonFileHandler("test.json")
    mock_open.assert_called_once_with("test.json", "w", encoding="utf-8")
    mock_open().write.assert_called_once_with("[]")


def test_reader(mock_open):
    mock_open.return_value.read.return_value = json.dumps([{"url": "http://some.com"}])

    handler = JsonFileHandler("test.json")
    data = handler.reader()

    assert data == [{"url": "http://some.com"}]

    assert mock_open.call_count == 2
    mock_open.assert_any_call("test.json", "w", encoding="utf-8")
    mock_open.assert_any_call("test.json", "r", encoding="utf-8")
