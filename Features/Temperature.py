from Body.Speak import Speak
import wolframalpha


def WolfRam(query):
    api_key = "T92W27-VVX4L9E2TP"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer

    except:
        Speak("The Value is Not Answerable")

def Temp(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("temperature", "")
    Term = Term.replace("what is the", "")
    Term = Term.replace("in", "")
    Term = Term.replace("tell", "")
    Term = Term.replace("me", "")
    Term = Term.replace("the", "")
    Term = Term.replace("current", "")

    tem_query = str(Term)


    if 'outside' in tem_query:
        var1 = 'Temperature in dholpur'
        answer = WolfRam(var1)
        Speak(f"{var1} is {answer}")

    else:
        var2 = "Temperature in" + tem_query
        ans = WolfRam(var2)
        Speak(f"{var2} is {ans}")
