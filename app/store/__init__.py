import typing
from app.store.crm.accessor import CrmAccessor

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_accessors(app: "Application"):
    app.crm_accessor = CrmAccessor()
