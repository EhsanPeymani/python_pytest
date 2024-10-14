def format_data_for_display(people):
    output = []
    for person in people:
        s1 = f"{person["given_name"]}"
        s2 = " " if person["given_name"] != "" and person["family_name"] != "" else ""
        s = s1 + s2 + f"{person["family_name"]}: {person["title"]}"
        output.append(s)
    return output


def format_data_for_excel(people):
    output = "given,family,title\n"
    for person in people:
        s = f"{person["given_name"]},{person["family_name"]},{person["title"]}\n"
        output += s
        
    return output


def connect(input):
    if input == 1:
        raise ConnectionError("Connection Error Raised")
    return 1
