from packit_app.table_elements import Female, Male, Username, UserGarmentSetting
import parse


@parse.with_pattern(r"\w+")
def parse_gender(gender_str: str):
    if gender_str.lower() == "female":
        return Female()
    elif gender_str.lower() == "male":
        return Male()

# @parse.with_pattern(r"\w+")
# def parse_gender_id(gender_str: str):
#     if gender_str.lower() == "female":
#         return GenderID(context.gender_table.get_matching_elements)


@parse.with_pattern(r"\w+")
def parse_username(name: str):
    return Username(name)


# @parse.with_pattern(r"\w+")
# def parse_user_garment_setting(user_garment_setting: str):
#     pass
