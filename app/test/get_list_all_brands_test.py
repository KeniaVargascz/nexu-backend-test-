import pytest
from unittest.mock import patch
from app.lambdas.get_list_all_brands import get_list_all_brands
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@pytest.mark.asyncio
async def test_get_list_all_brands():
    mock_data = [
        {
            "id": 1740,
            "name": "T-Cross",
            "average_price": 0,
            "brand_name": "Volkswagen"
        },
        {
            "id": 1741,
            "brand_name": "Toyota",
            "average_price": 45365465456,
            "name": "Upus"
        }
    ]

    with patch("app.layers.open_json", return_value=mock_data):
        result = await get_list_all_brands()
        logger.info(result)
        assert result[0]["brand_name"] == "Acura"
