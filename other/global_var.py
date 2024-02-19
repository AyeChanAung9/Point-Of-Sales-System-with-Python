my_db_name = "pos_database.db"


def set_db_name(db_name: str) -> None:
    global my_db_name
    my_db_name = db_name


def get_db_name() -> str:
    global my_db_name
    return my_db_name
