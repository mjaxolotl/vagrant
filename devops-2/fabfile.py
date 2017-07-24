from fabric.api import env

amount_container = 
env.hosts = ['devops@10.10.44.10']
env.passwords = {'devop@10.10.44.10s': '12345'}

# env.hosts = [ '10.10.44.10' ]
def hello(name="world"):
    print("Hello %s!" % name)
