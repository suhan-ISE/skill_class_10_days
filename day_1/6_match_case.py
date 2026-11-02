status = input("nim status eli (poor, middle, rich): ").strip().lower()

match status:
    case "poor":
        print("Mr beast du chaddi toli")
        
    case "middle":
        print("ooh namavru")
        
    case "rich":
        print("nim range ast nav ella bidi")
        
    case _:
        print("Enri media input adu?")
