from ping3 import ping


for i in range(1, 254):
    result_ping = ping(f'192.168.3.91')
    if result_ping != False:
        if result_ping != None:
            print(f'host up 200.200.1.3, {result_ping}')
    else:
        print(f'{result_ping}')