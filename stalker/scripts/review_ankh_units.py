import csv, re

NAME = "ankh_units"
DROP = set(range(9, 47)) | {48, 49, 65, 68, 70, 119, 120, 123, 130, 131, 134, 135, 139,
        147, 177, 178, 205, 239, 240, 241, 242, 243, 245, 250, 252, 273}
FIX = {
    67: "Wydarzenie",
    90: "➤2 graczy: użyjcie po 1 figurce Strażnika każdego rodzaju ➤3 graczy: użyjcie po 2 figurki Strażników każdego rodzaju ➤4 lub 5 graczy: użyjcie wszystkich dostępnych figurek Strażników każdego rodzaju (3 dla Strażników z małą podstawką, 2 dla Strażników z dużą podstawką).",
}
# proste podmiany w PL (literowki / rozbite slowa)
SUBS = {163: ("Uwiel- bienia", "Uwielbienia"), 174: ("(Amon- -Ra)", "(Amon-Ra)"),
        232: ("Chro- nioną", "Chronioną"), 249: ("WSZYS CY", "WSZYSCY")}

TAG = re.compile(r"【/?[BS]】|\[\[ICON\d+\]\]")
rows = {int(r["id"]): r for r in csv.DictReader(open(f"in/{NAME}.csv", encoding="utf-8-sig"))}
for i, (a, b) in SUBS.items():
    assert a in rows[i]["pl"], i
    FIX[i] = rows[i]["pl"].replace(a, b)
assert not DROP & FIX.keys()
for i, pl in FIX.items():
    assert sorted(TAG.findall(pl)) == sorted(TAG.findall(rows[i]["en"])), i

with open(f"out/{NAME}.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "decision", "pl_fixed"])
    for i in sorted(DROP | FIX.keys()):
        w.writerow([i, "DROP", ""] if i in DROP else [i, "FIX", FIX[i]])
print(len(rows), len(DROP), len(FIX))
