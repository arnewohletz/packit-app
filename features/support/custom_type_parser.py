from packit_app.elements import Female, Male
import parse


@parse.with_pattern(r"\w+")
def parse_gender(gender_str: str):
    if gender_str.lower() == "female":
        return Female()
    elif gender_str.lower() == "male":
        return Male()
