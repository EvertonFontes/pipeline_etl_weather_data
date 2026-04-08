import pytest
from unittest.mock import patch, MagicMock
import json
from pathlib import Path
import tempfile
import os
from src.extract_data import extract_weather_data


@pytest.fixture
def temp_data_dir(tmp_path):
    """Fixture to provide a temporary directory for data files."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    return data_dir


@patch('src.extract_data.requests.get')
def test_extract_weather_data_success(mock_get, temp_data_dir, caplog):
    """Test successful extraction of weather data."""
    # Mock the response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"temperature": 25, "humidity": 60}]
    mock_get.return_value = mock_response

    # Change to temp directory for testing
    original_cwd = os.getcwd()
    os.chdir(temp_data_dir.parent)
    try:
        result = extract_weather_data("http://example.com/weather")

        # Check return value
        assert result == [{"temperature": 25, "humidity": 60}]

        # Check file was created and content
        output_file = Path("data/weather_data.json")
        assert output_file.exists()
        with open(output_file, "r") as f:
            saved_data = json.load(f)
        assert saved_data == [{"temperature": 25, "humidity": 60}]

    finally:
        os.chdir(original_cwd)


@patch('src.extract_data.requests.get')
def test_extract_weather_data_request_failure(mock_get, caplog):
    """Test extraction when request fails."""
    # Mock the response
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    result = extract_weather_data("http://example.com/weather")

    # Check return value
    assert result == []

    # Check logging
    assert "Erro na requisição" in caplog.text


@patch('src.extract_data.requests.get')
def test_extract_weather_data_empty_data(mock_get, temp_data_dir, caplog):
    """Test extraction when response returns empty data."""
    # Mock the response
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = []
    mock_get.return_value = mock_response

    # Change to temp directory for testing
    original_cwd = os.getcwd()
    os.chdir(temp_data_dir.parent)
    try:
        result = extract_weather_data("http://example.com/weather")

        # Check return value
        assert result == []

        # Check file was created with empty data
        output_file = Path("data/weather_data.json")
        assert output_file.exists()
        with open(output_file, "r") as f:
            saved_data = json.load(f)
        assert saved_data == []

        # Check logging
        assert "Nenhum dado retornado" in caplog.text
    finally:
        os.chdir(original_cwd)