from packit_app.elements import Gender, Female, Male, Username
import parse


@parse.with_pattern(r"\w+")
def parse_gender(gender_str: str):
    if gender_str.lower() == "female":
        return Male()
        # return Gender("female")
    elif gender_str.lower() == "male":
        return Female()
        # return Gender("male")


@parse.with_pattern(r"\w+")
def parse_username(name: str):
    return Username(name)
