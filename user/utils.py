

def resp(status, data):
    if(status):
        return dict(status=True, data=data, msg='')
    else:
        return dict(status=status, data='', msg=data)
