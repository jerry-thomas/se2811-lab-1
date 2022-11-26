import os
import requests
import json

COOKIE = '_ga=GA1.2.491132621.1629919515; rce.htmleditor=PRETTY; fs_uid=rs.fullstory.com#S28S2#5568706929074176:5026071942373376#79b5209e#/1666664707; log_session_id=72cff7cfb95ce4396d2d93c2fe1b5c95; _legacy_normandy_session=IR1qeteg1waI2IyK9gqm7w+uFxtsmWmgijpdwRWfOyqh7DBv9WUBl9ctCRJmRDAlxZwNKgs_H5FtejcP1oc9_XIVdF5MjVt4wnSaF-fxXF8_DChQ515-pQh8ZIVE-qiezXsWmO3HauoywkAAM5vkJqdvqGx1dFjB3tOMda3qBWeb8KyNyvO2lBfOQ4YH1GbSphRH10qo__U_cSxeMYTu810Aeddsz5WyXI8anYrSNwhmskg__A751YjceH-ogOnAh4JxFVjahFwb3Y50Jk3UHpXd7diYSu5NsvOoRvrHDxe3F0x_OqrR96qBAaImS00k44OfyDYDI5KiVKStAkiJjKm3qG82xQohECtjozZJ86U5F7er5Cqwx_w-OzzQ59WvDtAsybAQ_NhUR2PbKVdY3MvO5o6USf7kkpIsimJlEOtTp29nF-F2XiuIh2a_mGszm4geBqIIofDshnN1GDKPY59tISH_883W1PzrOV0HWYvOIl9Y0NuwVoxRXc56UeIvqlzANbXRML5odgManYTjrRVuDSglhFyCNwu97aXuu5mdbIChcX8yLMDDiT39AIx7hIYdqEwUR8dUivhtBCBAdUP.AtYJpk6Tcm4_Gmjoe5gyJE6aahs.YZQMbw; canvas_session=IR1qeteg1waI2IyK9gqm7w+uFxtsmWmgijpdwRWfOyqh7DBv9WUBl9ctCRJmRDAlxZwNKgs_H5FtejcP1oc9_XIVdF5MjVt4wnSaF-fxXF8_DChQ515-pQh8ZIVE-qiezXsWmO3HauoywkAAM5vkJqdvqGx1dFjB3tOMda3qBWeb8KyNyvO2lBfOQ4YH1GbSphRH10qo__U_cSxeMYTu810Aeddsz5WyXI8anYrSNwhmskg__A751YjceH-ogOnAh4JxFVjahFwb3Y50Jk3UHpXd7diYSu5NsvOoRvrHDxe3F0x_OqrR96qBAaImS00k44OfyDYDI5KiVKStAkiJjKm3qG82xQohECtjozZJ86U5F7er5Cqwx_w-OzzQ59WvDtAsybAQ_NhUR2PbKVdY3MvO5o6USf7kkpIsimJlEOtTp29nF-F2XiuIh2a_mGszm4geBqIIofDshnN1GDKPY59tISH_883W1PzrOV0HWYvOIl9Y0NuwVoxRXc56UeIvqlzANbXRML5odgManYTjrRVuDSglhFyCNwu97aXuu5mdbIChcX8yLMDDiT39AIx7hIYdqEwUR8dUivhtBCBAdUP.AtYJpk6Tcm4_Gmjoe5gyJE6aahs.YZQMbw; _csrf_token=7yRilp4KQdzQeOmd3xKguHJimi5G4xl+Pb0M++eQCgOfVjHn92wSlLkvu/rrY9DrGhuuGBWidhwF0WODispQNA=='

API_ENDPOINT = 'https://msoe.instructure.com/api/v1/'


def get_json_request(request_url, data=None):
    headers = dict()
    headers['cookie'] = COOKIE

    if data is not None:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(data)

    response = requests.get(request_url, data=data, headers=headers)
    if response.status_code != 200:
        raise Exception("Bad response status: {}".format(response.status_code))

    return json.loads(response.text), response.headers


def get_course_assignment(course_id, assignment_id):
    return get_json_request('{}courses/{}/assignments/{}'.format(API_ENDPOINT, course_id, assignment_id)),


def parse_link_header(headers):
    if headers['Link'] is None:
        return None

    def split_strip(value, delimiter):
        return list(map(lambda x: x.strip(), value.split(delimiter)))

    links = split_strip(headers['Link'], ',')
    for link in links:
        link_elements = split_strip(link, ';')
        if link_elements[1] == 'rel="next"':
            return link_elements[0][1:-1]
    return None


def get_course_files(course_id):
    files = []
    files_url = '{}courses/{}/files'.format(API_ENDPOINT, course_id)
    while files_url is not None:
        results, headers = get_json_request(files_url)
        files += results
        files_url = parse_link_header(headers)
    return files


for x in get_course_files(8426):
    print(x['display_name'])

#for x in get_course_files(8426):
#    print(x["filename"])