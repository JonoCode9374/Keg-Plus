#utf-8
#The Uncompressor

def Uncompress(source):
    result = ""
    string_type = ""
    temp = {"type" : None, "data" : ""}
    cont = False
    
    for char in source:
        if cont:
            cont = False
            continue
        if string_type != "":
            if char is string_type:
                string_type = ""
                result += standard(temp)
                temp = {"type" : None, "data" : ""}
            else:
                temp["data"] += char

        elif char == "\\":
            temp["data"] += char
            cont = True
            continue

        elif char in "`¶‘“«„":
            string_type = char
            #temp["data"] += char
            temp["type"] = char

        else:
            result += char

    return result

def standard(string):
    result = "`"
    escaped = False
    print(string["type"])
    
    if string["type"] == "`":
        code = ""
        for char in string["data"]:
            if escaped:
                escaped = False
                continue
            elif char == ";":
                if len(code) == 2:
                    result += f"<SCC:{code}>"
                else:
                    result += code + ";"

                code = ""
            elif char == "\\":
                escaped = True
                continue

            elif len(code) == 2:
                result += code[0]
                code = code[1] + char

            else:
                code += char
    elif string["type"] == "¶":
        code = ""
        escpaed = False
        for char in string["data"]:
            if escaped:
                escaped = False
                continue
            elif char == ";":
                if len(code) == 2:
                    result += f"<SCC:{code}>"
                    result += " "
                else:
                    result += code + ";"

                code = ""
            elif char == "\\":
                escaped = True
                continue

            elif len(code) == 2:
                result += code[0]
                code = code[1] + char

            else:
                code += char

    elif string["type"] == "\u2018":
        if len(string["data"]) % 2 != 0:
            string["data"] += " "

        print(string["data"])
        for scc in [string["data"][i:i+2] for i in range\
                    (0, len(string["data"]), 2)]:
            result += f"<SCC:{scc}>"

    elif string["type"] == "“":
        pass

    return result + "`"
