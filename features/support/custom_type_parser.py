from packit_app.table_elements import Female, Male, Username
import parse


@parse.with_pattern(r"\w+")
def parse_gender(gender_str: str):
    if gender_str.lower() == "female":
        return Female()
    elif gender_str.lower() == "male":
        return Male()


@parse.with_pattern(r"\w+")
def parse_username(name: str):
    return Username(name)
