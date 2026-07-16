def is_relevant(title, description):

    keywords = [
        "merger",
        "mergers",
        "acquisition",
        "acquisitions",
        "investment",
        "investments",
        "strategic investment",
        "stake",
        "strategic stake",
        "buyout",
        "joint venture",
        "funding",
        "expansion",
        "fmcg",
        "consumer goods",
        "unilever",
        "nestle",
        "hindustan unilever",
        "hul",
        "itc",
        "britannia",
        "dabur",
        "marico",
        "godrej consumer",
        "emami",
        "pepsico",
        "coca-cola"
    ]

    text = f"{title} {description}".lower()

    for keyword in keywords:
        if keyword in text:
            print("Relevant:", title)
            return True

    print("Not Relevant:", title)
    return False