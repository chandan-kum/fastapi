def individual_serisl(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "cname": user["cname"],
        "lscore": user["lscore"],
        "phone": user["phone"],
        "location": user["location"],
        "tags": user["tags"],
        "date": user["date"],
        
    }


def list_serials(users):
    return[individual_serisl(user) for user in users]
