
import requests
def data(srn):
    s = "https://registrations.sakshamalok.repl.co/srn/" + srn
    r = requests.get(s).json()
    # print(r)
    print(r['name'])
# f = True
# while(f):
#     srn = input()
#     # print(srn)
#     if srn == "no" :
#         f = False
#     data(srn)

