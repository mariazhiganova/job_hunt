from unittest.mock import MagicMock, patch


@patch("requests.get")
def test_hh_connection_success(mock_get, hh):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"id": 1, "name": "Разработчик"}, {"id": 2, "name": "Дизайнер"}]}
    mock_get.return_value = mock_response

    vacancies = hh._HH__connection()

    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Разработчик"


@patch("requests.get")
def test_hh_connection_error(mock_get, hh):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.reason = "Not Found"
    mock_get.return_value = mock_response

    vacancies = hh._HH__connection()

    assert vacancies == []
