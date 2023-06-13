from typing import TYPE_CHECKING, Literal, Optional, Union

import pydantic
from pydantic import AnyUrl

from great_expectations.core._docs_decorators import public_api
from great_expectations.datasource.fluent import SQLDatasource
from great_expectations.datasource.fluent.config_str import ConfigStr

if TYPE_CHECKING:
    from great_expectations.compatibility.sqlalchemy import (
        sqlalchemy as sa,
    )


class RedshiftDsn(pydantic.PostgresDsn):
    allowed_schemes = {
        "redshift",
        "redshift+redshift_connector",
        "redshift+psycopg2",
    }


@public_api
class Redshift(SQLDatasource):
    """Adds a redshift datasource to the data context.

    Args:
        name: The name of this postgres datasource.
        connection_string: The SQLAlchemy connection string used to connect to the postgres database.
            For example: "redshift+redshift_connector://redshift:@localhost/test_database"
        connect_args: An optional dictionary of connection args for redshift which is passed to
            sqlalchemy `create_engine()`.
        assets: An optional dictionary whose keys are TableAsset or QueryAsset names and whose values
            are TableAsset or QueryAsset objects.
    """

    type: Literal["redshift"] = "redshift"  # type: ignore[assignment] # base class is expecting 'sql'
    connection_string: Union[ConfigStr, RedshiftDsn]
    # connect_args
    iam: bool = True
    credentials_provider: Optional[str] = None
    idp_host: Optional[AnyUrl] = None
    app_id: Optional[str] = None
    app_name: Optional[str] = None
    region: Optional[str] = None
    cluster_identifier: Optional[str] = None
    ssl_insecure: bool = False

    def get_engine(self) -> sa.engine.Engine:
        # TODO: implement this
        return super().get_engine()