def team_dinner(team_dates):
    if not all(isinstance(date, list) for date in team_dates):
        return None

    all_of_dates = sum(team_dates, [])
    try:
        dates = {
                n: {
                    "attendance": all_of_dates.count(n),
                    "flexibility": sum(len(person) for person in team_dates if n in person)
                    }
                for n in range(max(all_of_dates) + 1)
                }
    except ValueError:
        return None
    
    max_attendance = 0
    for date_attributes in dates.values():
        if date_attributes["attendance"] > max_attendance:
            max_attendance = date_attributes["attendance"]

    # print("MAX ATTENDANCE:", max_attendance)

    if max_attendance >= len(team_dates) - max_attendance:
        days_with_max_attendance = []
        for date, date_attributes in dates.items():
            if date_attributes["attendance"] == max_attendance:
                days_with_max_attendance.append(date)

        # print("DAYS WITH MAX ATTENDANCE:", days_with_max_attendance)

        if len(days_with_max_attendance) == 1:
            return days_with_max_attendance[0]
            
        elif len(days_with_max_attendance) > 1:
            dates_2 = {}
            for key in days_with_max_attendance:
                if key in dates:
                    dates_2[key] = dates[key]

            max_flexibility = 0
            for date_attributes in dates_2.values():
                if date_attributes["flexibility"] > max_flexibility:
                    max_flexibility = date_attributes["flexibility"]

            # print("MAX FLEXIBILITY:", max_flexibility)
                
            days_with_max_flexibility = []
            for date, date_attributes in dates_2.items():
                if date_attributes["attendance"] == max_attendance:
                    if date_attributes["flexibility"] == max_flexibility:
                        days_with_max_flexibility.append(date)
            
            # print("DAYS WITH MAX FLEXIBILITY:", days_with_max_flexibility)
            
            if days_with_max_flexibility:
                return days_with_max_flexibility[0]
            else:
                return None

        return None


print(team_dinner([[0, 3, 8, 11, 10, 7, 1, 5, 2, 9], [11, 8], [4], [6, 3, 11, 8, 5, 10, 1, 2, 4, 9], [1, 9, 8, 3, 10, 4, 0, 6, 5, 2], [9, 0, 3, 10, 4, 5, 8, 7, 2], [1, 11, 10, 4, 8], [8], [10, 5, 0, 9, 2, 6, 1, 4], [4]]))



