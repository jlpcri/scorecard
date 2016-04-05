def get_model_fields(cls, key, level):
    exclusion_list = ''
    if level == 'person':
        exclusion_list = ['id', 'human_resource', 'created', 'confirmed', 'updated']
    elif level == 'team':
        exclusion_list = ['id', 'functional_group', 'subteam', 'created', 'confirmed', 'updated',
                          'staffs', 'contractors', 'openings']
    data = ()
    fields = cls._meta.get_fields()
    for field in fields:
        if field.name not in exclusion_list:
            data += ((field.name, field.verbose_name),)

    return data
