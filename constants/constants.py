
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

# current goal: get dps for entire raid
#enums don't go in quotes
GET_LAST_RAID_LOG_QUERY = """
    query($fightIDs: [Int]!){
        reportData {
            reports(guildName: "NinetyNineParse", guildServerSlug: "Sargeras", guildServerRegion: "us", limit: 1) {
                data {
                    table(fightIDs: $fightIDs, killType: Encounters, dataType: DamageDone) 
                }
            }
        }
    }
"""

GET_FIGHT_IDS_QUERY = """
    {
        reportData {
            reports(guildName: "NinetyNineParse", guildServerSlug: "Sargeras", guildServerRegion: "us", limit: 1) {
                data {
                    fights (killType: Encounters){
                        id
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