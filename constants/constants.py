
NORMAL_DIFFICULTY = 3
HEROIC_DIFFICULTY = 4
MYTHIC_DIFFICULTY = 5
REPORT_CODE = "cwjn231DBfRJyMmA"


TEST_QUERY = """
    query($code: String, $difficulty: Int){
        reportData {
            report(code: $code) {
                fights(difficulty: $difficulty) {
                    id
                    name
                }
            }
        }
    }
"""
# report(code:{REPORT_CODE}, difficulty:{NORMAL_DIFFICULTY}) {{
        #     id
        #     name
        #     startTime
        #     endTime
        # }}
# query = f"""
#             {{
#                 characterData {{
#                     character(name: "{char_name}", serverSlug: "{server_slug}", serverRegion: "us") {{
#                         name
#                         classID
#                         server {{
#                             name
#                         }}
#                     }}
#                 }}
#             }}
#     """