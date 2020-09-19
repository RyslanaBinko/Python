def None_in_the_dict():
    d_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
    return dict((key, value) for key, value in d_dict.items() if value is not None)

print(None_in_the_dict())


