from suds.client import Client
hello_client = Client('http://localhost:7789/?wsdl')
hello_client.options.cache.clear()
rules={}
rules["username"]="alle"
rules["emotion"]="1-2-3"

print rules
result = hello_client.service.get_recommend(rules)
print result

hiString = hello_client.service.get_hi("lily")
print hiString

bobstring = hello_client.service.get_graph("bob")
print bobstring