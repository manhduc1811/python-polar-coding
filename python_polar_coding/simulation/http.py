import requests


def prepare(url, snr_range, required_messages, nodes,
            repetitions=1,
            code_types=None,
            code_lengths=None):
    params = {
        'code_types': code_types,
        'code_lengths': code_lengths,
        'snr_range': snr_range,
        'required_messages': required_messages,
        'nodes': nodes,
        'repetitions': repetitions,
    }
    try:
        return requests.post(f'{url}/prepare', json=params)
    except Exception as e:
        print(e)


def get_params(url, experiments):
    try:
        resp = requests.put(f'{url}/get-params', json={'experiments': experiments})
        return resp.json()
    except Exception as e:
        print(e)


def save_result(url, result, code_id, code_type, channel_type):
    result.update({'route_params': {
        'code_id': code_id,
        'code_type': code_type,
        'channel_type': channel_type,
    }})
    try:
        requests.post(f'{url}/save-result', json=result)
    except Exception as e:
        print(e)
