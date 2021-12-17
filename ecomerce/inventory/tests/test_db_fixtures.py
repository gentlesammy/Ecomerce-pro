import pytest
from ecomerce.inventory import models

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (16, "phones", "phones", 1),
        (26, "home", "home", 1),

    ]
)
def test_inventory_category_dbfixtures(
    db, django_db_setup, 
): 
    pass