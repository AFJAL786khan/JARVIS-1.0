from Body.Speak import Speak
import wolframalpha

def Wolfram(query):
    api_key = "T92W27-VVX4L9E2TP"
    client = wolframalpha.Client(api_key)
    res = client.query(query)

    try:
        answer = next(res.results).text
        return answer

    except StopIteration:
        Speak("The answer is not available")


def Calco(query):
    term = str(query)
    term = term.replace("jarvis", "")
    term = term.replace("multiply", "*")
    term = term.replace("plus", "+")
    term = term.replace("minus", "-")
    term = term.replace("divide", "/")
    term = term.replace("into", "*")

    final = str(term)

    try:
        result = Wolfram(final)
        print(result)
        Speak(result)

    except:
        Speak("The answer is not available")



