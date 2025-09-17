
NORMAL_DIFFICULTY = 3
HEROIC_DIFFICULTY = 4
MYTHIC_DIFFICULTY = 5
REPORT_CODE = "cwjn231DBfRJyMmA"


TEST_QUERY = """
    query($guildName: String, $guildServerSlug: String, $difficulty: Int){
        reportData {
            reports(guildName: $guildName. guildServerSlug: $guildServerSlug, serverRegion: "us") {
                fights(difficulty: $difficulty) {
                    id
                    name
                }
            }
        }
    }
"""

GUILD_QUERY = """
    query($guildName: String, $guildServerSlug: String){
        reportData {
            reports(guildName: $guildName, guildServerSlug: $guildServerSlug, guildServerRegion: "us", limit: 5) {
                data {
                    title
                    guild {
                        name
                    }
                    zone {
                        id
                        name
                    }
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