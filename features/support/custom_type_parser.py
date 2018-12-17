from packit_app.elements import Gender, Female, Male
import parse


@parse.with_pattern(r"\w+")
def parse_gender(gender_str: str):
    if gender_str.lower() == "female":
        return Gender("female")
    elif gender_str.lower() == "male":
        return Gender("male")
