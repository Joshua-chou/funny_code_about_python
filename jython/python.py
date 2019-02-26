import requests
import sys

def my_test(name):
    print("name: "+name)
    return "success"

my_test(sys.argv[1])




