import typing


if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    from .views import AddUserView, ListUsersView

    app.router.add_view("/add_user", AddUserView)
    app.router.add_view("/list_users", ListUsersView)
