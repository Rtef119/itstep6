class Build_error(Exception):
    def __str__(self):
        return f"Z ziey kilkisty zeglu bobydybatu dim ne mozluvo!"

def perevirka (kilkist, limit):
    if kilkist>limit:
        return "Wustazae"
    else:
        raise Build_error(kilkist)

zegla = 150
perevirka(zegla,1000)