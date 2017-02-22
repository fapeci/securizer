import pandas as pd
df = pd.read_csv('permissions.csv')
potentially_unsecure_apps = []
unsecure_apps = []
for index, row in df.iterrows():
    if row['Permissions'] == 'Internet Access':
        potentially_unsecure_apps.append(row['Apps']+':'+str(index))
print potentially_unsecure_apps
for index, row in df.iterrows():
    str_index = str(index)
    for apps in potentially_unsecure_apps:
        app = apps.split(':')[0]
        app_index = apps.split(':')[1]
        row_apps = row['Apps']
        row_permissions = row['Permissions']
        if not str_index == app_index and row_apps == app and not row_permissions == 'Internet Access':
                unsecure_apps.append(row['Apps'])
print unsecure_apps