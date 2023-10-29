file_name = input('File name: ')
new_file_name = file_name.lower().strip()
new_file_name = new_file_name.split('.')[-1]
match new_file_name:
    case 'gif':
        print('image/gif')
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case _:
        print('application/octet-stream')