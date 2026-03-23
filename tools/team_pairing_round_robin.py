import csv

def round_robin_schedule(people, rounds, cycle_length=2):
    """
    Erstellt einen Round-Robin-Plan fuer Team-Pairings.
    
    people: Liste aller Teammitglieder
    rounds: Anzahl der Pairing-Runden
    cycle_length: Dauer einer Runde in Wochen
    """
    n = len(people)
    if n % 2 != 0:
        people.append("Freilos")  # bei ungerader Anzahl

    # Initiale Reihenfolge (fix)
    roster = people[:]
    schedule = []

    for r in range(rounds):
        pairs = []
        for i in range(n // 2):
            pair = (roster[i], roster[n - 1 - i])
            if "Freilos" not in pair:
                pairs.append(pair)
        schedule.extend(pairs)

        # Rotation (Round-Robin)
        # erstes Element bleibt fix, der Rest rotiert
        roster = [roster[0]] + [roster[-1]] + roster[1:-1]

    return schedule

def print_schedule_kw(schedule, start_kw=1, cycle_length=2):
    """
    Gibt den Plan mit Kalenderwochen aus.
    start_kw: Start-Kalenderwoche (z.B. 14)
    cycle_length: Dauer eines Zyklus in Wochen
    """
    kw = start_kw
    for pair in schedule:
        end_kw = kw + cycle_length - 1
        print(f"KW{kw}-KW{end_kw}: {pair[0]} + {pair[1]}")
        kw += cycle_length

def export_to_csv_kw(schedule, filename="pair_schedule.csv", start_kw=1, cycle_length=2):
    """
    Exportiert den Plan als CSV mit Kalenderwochen
    """
    kw = start_kw
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Start KW", "End KW", "Person 1", "Person 2"])

        for pair in schedule:
            end_kw = kw + cycle_length - 1
            writer.writerow([kw, end_kw, pair[0], pair[1]])
            kw += cycle_length

    print(f"CSV erfolgreich erstellt: {filename}")


# =========================
# CONFIG
# =========================
people = ["A", "B", "C", "D", "E", "F", "G"]    # Team-Mitglieder
rounds = 9                                      # Anzahl der Runden
cycle_length = 2                                # Dauer des Pairings
start_kw = 14                                   # z.B. Start in Kalenderwoche 14

# =========================
# RUN
# =========================
schedule = round_robin_schedule(people, rounds)
print_schedule_kw(schedule, start_kw, cycle_length)
export_to_csv_kw(schedule, "pair_schedule.csv", start_kw, cycle_length)