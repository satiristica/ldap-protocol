from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DataTable
from textual.binding import Binding
from src.database import get_all_employees


class EmployeeDirectoryApp(App):
    TITLE = "LDAP Employee Directory"
    BINDINGS = [
        Binding("u", "refresh_database", "Refresh DB"),
        Binding("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable()
        yield Footer()

    def on_mount(self):
        table = self.query_one(DataTable)

        table.add_columns(
            "ID",
            "Name",
            "Email",
            "Title",
            "Department"
        )

        self.load_table()

    def action_refresh_database(self):
        try:
            self.load_table()
        except Exception as error:
            self.notify(f"Database refresh failed: {error}", severity="error")
            return

        self.notify("Database refreshed")

    def load_table(self):
        table = self.query_one(DataTable)

        table.clear()

        employees = get_all_employees()

        for employee in employees:
            table.add_row(
                str(employee[0]),
                employee[1],
                employee[2],
                employee[3],
                employee[4],
            )


if __name__ == "__main__":
    EmployeeDirectoryApp().run()
