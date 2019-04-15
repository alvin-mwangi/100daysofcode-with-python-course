import research

def main():
    print("Weather research for Seattle, 2014-2015")
    print()
    research.init()

    print("The hottest 5 days:")
    days = research.hot_days()
    for idx, d in enumerate(days[:5]):
        print(f"{idx+1}. {d.actual_max_temp} F on {d.date}")
    
    print()
    print("The coldest 5 days:")
    days = research.cold_days()
    for idx, d in enumerate(days[:5]):
        print(f"{idx+1}. {d.actual_min_temp} F on {d.date}")
    
    print("The wettest 5 days:")
    days = research.wet_days()
    for idx, d in enumerate(days[:5]):
        print(f"{idx+1}. {d.actual_precipitation} inches of rain on {d.date}")
    
if __name__ == "__main__":
    main()

